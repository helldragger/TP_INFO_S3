import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

points = np.zeros((0,2))

fig = plt.figure()
def updatefig(i):
	global points
	fig.clear()
	plt.scatter(points[:,0],points[:,1],color='b',marker='s',s=5,alpha=0.5)
	x = np.random.randn(50,2)
	plt.scatter(x[:,0],x[:,1],color='b',marker='s',s=5)
	plt.draw()
	points = np.concatenate([points,x],axis=0)

anim = animation.FuncAnimation(fig, updatefig, 20)	
anim.save("test.mp4", fps=5)