from random import randint

# CONSTANTS
# DATA FORMAT; BORDER|ADDR_S|ADDR_R|SIZE  |MESG  |SEC1
# LENGTHS ===> BORD_S|===ADDR_S=== |SIZE_S|MESG_S|SEC1_S <- variable
BORDER = "01111110"
BORD_S = len(BORDER)
SIZE_S = 8
ADDR_S = 4 * 2

DP_BLOCK_SIZE = 4

CRC_GX = "11001"

PBIT = "pb"
DPBIT = "dpb"
CRC = "crc"

SEC = CRC

# UTILITAIRE

def int_to_bin_str(x, size):
    n = str(bin(x))[2:]
    return "".join(["0" * (size - len(n)), n])


def bin_str_to_int(s):
    return int('0b' + s, 2)


# COUCHE 2 - intermediaire

def gen_identification(trnsm, recpt):
    return "".join([int_to_bin_str(trnsm, ADDR_S//2),
                    int_to_bin_str(recpt, ADDR_S//2)])


def get_sender(mess):
    """
    Get the sender from a binary message

    :param mess: couche 2 + couche 1 data
    :return: sender from couche 2 data
    """
    return bin_str_to_int(mess[BORD_S:BORD_S + ADDR_S//2])


def is_adressed_to_me(mess, self_addr):
    return bin_str_to_int(mess[BORD_S + ADDR_S//2:BORD_S + ADDR_S]) == self_addr


# COUCHE 2 - DATA ERROR DETECTION

def gen_parity_bit(msg):
    return str(int(msg.count('1') % 2))


def gen_dparity_bits(msg):
    from math import ceil
    pbit_row = ""
    pbit_col = ""
    nb_rows = int(ceil(len(msg)/DP_BLOCK_SIZE))

    for i in range(nb_rows):
        if i + nb_rows > len(msg):
            row = msg[i:]
        else:
            row = msg[i:i+nb_rows]
        pbit_row += str(int(row.count('1') % 2))

    for i in range(DP_BLOCK_SIZE):
        col = ""
        for j in range(nb_rows):
            if j * nb_rows + i >= len(msg):
                break
            else:
                col += msg[j*nb_rows + i]
        pbit_col += str(int(col.count('1') % 2))

    return pbit_row, pbit_col


def get_dparity_size(msg_length):
    from math import ceil
    return int(ceil(msg_length/DP_BLOCK_SIZE) + DP_BLOCK_SIZE)

def gen_crc(msg_bin, key='0'*len(CRC_GX)):
    msg_bin += key
    result = ""
    for i in range(len(CRC_GX)):
        msg_bin = int('0b'+msg_bin) ^ int('0b'+CRC_GX,2)
    while len(msg_bin) >=len(CRC_GX):
        XOR_str = msg_bin[0:len(CRC_GX)]
        msg_bin = msg_bin[1:]
        for i in range(len(string)):
            msg_bin[i] = str(int(bool(string[i]) ^ bool(CRC_GX[i])))
    return msg_bin


# COUCHE 2 - DATA ERROR CORRECTION

def regen_hamming():
    pass

# COUCHE 2 - CODEX

# cette fonction traduit un message en une trame/sequence de bits. Cette fonction est maintenant simple, mais elle est
# insuffisante (elle ne permet pas de trouver le debut du message par exemple) le but de ce TP est de la completer.
def couche2(message_from_sender, sender, receipter):
    # generate identification
    auth = gen_identification(sender, receipter)

    # translate message into binary data
    msg = message_from_sender.replace("o", "0").replace("i", "1")

    # get data length to binary
    size_b = int_to_bin_str(len(msg), SIZE_S)

    # gen security
    if SEC == PBIT:
        security = "".join(gen_parity_bit(msg))
    elif SEC == DPBIT:
        security = "".join(gen_dparity_bits(msg))
    elif SEC == CRC:
        security = "".join(gen_crc(msg))
    else:
        security = ""

    # Returns Border + auth + whole message + security.
    return "".join([BORDER,
                    auth,
                    size_b,
                    msg,
                    security])


# cette fonction traduit une sequence de bits en un message. Cette fonction est maintenant simple, mais elle est
# insuffisante (elle ne permet pas de trouver le debut du message par exemple) le but de ce TP est de la completer.
def couche2R(message_from_sender, receipter):
    # Find beginning of message
    begin_i = message_from_sender.find(BORDER)
    # Verify if the message is addressed to us (adresses)
    if is_adressed_to_me(message_from_sender[begin_i: begin_i+BORD_S+ADDR_S],
                         receipter):

        data = message_from_sender[begin_i::]

        # get data length
        MSG_S = bin_str_to_int(
                    message_from_sender[begin_i+BORD_S+ADDR_S:
                                        begin_i+BORD_S+ADDR_S+SIZE_S])
        # get data
        msg = message_from_sender[begin_i+BORD_S+ADDR_S+SIZE_S:
                                  begin_i+BORD_S+ADDR_S+SIZE_S+MSG_S]
        # Get parity bit
        if SEC == PBIT:
            pbit = data[BORD_S + ADDR_S + SIZE_S + MSG_S:
                        BORD_S + ADDR_S + SIZE_S + MSG_S + 1]
            if pbit != gen_parity_bit(msg):
                print("Parity bit incorrect: data corrupted")
        elif SEC == DPBIT:
            dp = data[BORD_S + ADDR_S + SIZE_S + MSG_S:
                      BORD_S + ADDR_S + SIZE_S + MSG_S + get_dparity_size(MSG_S)]
            dp_row, dp_col = dp[:-DP_BLOCK_SIZE:1], dp[-DP_BLOCK_SIZE::1]
            if (dp_row, dp_col) != gen_dparity_bits(msg):
                print("Double parity bits incorrect: data corrupted")
        elif SEC == CRC:
            crc = data[BORD_S + ADDR_S + SIZE_S + MSG_S:
                       BORD_S + ADDR_S + SIZE_S + MSG_S + len(CRC_GX)]
            if "0"*len(CRC_GX) != gen_crc(msg, crc):
                print("CRC incorrect: data corrupted")
        else:
            pass
        return msg.replace("0", "o").replace("1", "i")
    else:
        return "Message ignored"



# COUCHE 1 - CODEX

# cette fonction represente la tradution faite par le codage NRZ
def couche1(trame_de_bits):
    return trame_de_bits.replace("0", "-").replace("1", "+")


def couche1_man(trame_de_bits):
    return trame_de_bits.replace("0", "-+").replace("1", "+-")


# cette fonction represente la tradution faite par le codage NRZ
def couche1R(trame_de_bits):
    return trame_de_bits.replace("-", "0").replace("+", "1")


def couche1R_man(trame_de_bits):
    res = ""
    temp = ""
    for bit_i in range(len(trame_de_bits)):
        temp += trame_de_bits[bit_i]
        if len(temp) == 2:
            if temp == "-+":
                res += "0"
                temp = ""
            elif temp == "+-":
                res += "1"
                temp = ""
            else:
                temp = temp[1:]

    return res


# SIMULATION


def signal_swap_error(signal, n):
    if n >= len(signal):
        return signal
    if signal[n] == '+':
        return "".join([signal[:n], '-', signal[n + 1:]])
    return "".join([signal[:n], '+', signal[n + 1:]])


# cette fonction simule le canal. Le canal contient initialement du bruit: le recepteur etait a l'ecoute avant que l'emetteur n'envoie son message.
# Il contient aussi un bruit final, car le recepteur sera aussi a l'ecoute apres l'envoi du message.
# Le defi de la couche 2 est de permettre au recepteur de determiner ou commence et ou termine le message envoye.
def transmission(signal_from_sender):
    # bruit initial
    for x in range(0, randint(4, 10)):
        if randint(0, 1) == 1:
            signal_from_sender = "-" + signal_from_sender
        else:
            signal_from_sender = "+" + signal_from_sender

    # bruit final
    for x in range(0, randint(4, 10)):
        if randint(0, 1) == 1:
            signal_from_sender = signal_from_sender + "-"
        else:
            signal_from_sender = signal_from_sender + "+"

    return signal_from_sender


def emission(message_from_sender, sender_addr, receipter_addr):
    print("message a envoyer:" + message_from_sender)
    trame_de_bits_envoyee = couche2(message_from_sender, sender_addr, receipter_addr)
    print("trame a envoyer:" + trame_de_bits_envoyee)
    print("trame length:", len(trame_de_bits_envoyee), "; data length:", len(message_from_sender))
    signal_envoye = couche1(trame_de_bits_envoyee)
    print("signal envoye:" + signal_envoye)
    return signal_envoye


def reception(signal_sur_canal, receipter_addr):
    print("signal entendu, avec le bruit:" + signal_sur_canal)
    bits_recus = couche1R(signal_sur_canal)
    print("bits recus par le recepteur:" + bits_recus)
    message_recu = couche2R(bits_recus, receipter_addr)
    print("message recu par le recepteur:" + message_recu)
    return message_recu


def simulation(message_from_sender):
    sender_addr = 1
    receipter_addr = 3
    cible_addr = 3
    signal_envoye = emission(message_from_sender, sender_addr, cible_addr)
    signal_sur_canal = transmission(signal_envoye)
    #signal_sur_canal = signal_swap_error(signal_sur_canal, 30)
    return reception(signal_sur_canal, receipter_addr)

message = "iiiioiiiooooioiioio"
result = simulation(message)
print("COMPARAISON DES MESSAGES")
print("msg sent:\t\t", message)
print("received:\t\t", end=" ")
len_m = len(message)
len_r = len(result)
for char_i in range(max(len_r, len_m)):
    if char_i >=len_r:
        #missing char in result
        print('-', end="")
    elif char_i >= len_m:
        #added chars
        print('+', end="")
    elif message[char_i] == result[char_i]:
        print("x", end="")
    else:
        print(result[char_i], end="")

