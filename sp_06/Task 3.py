import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

def f(x,y): 
    return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(-np.pi,np.pi/2,n)

[X,Y]=np.meshgrid(x,y)
z=f(X,Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax = p3.Axes3D(fig)
M=ax.plot_surface(X,Y+(np.pi),z,cmap='gist_ncar')
ax.set_xlim3d([-np.pi/2,np.pi/2])
ax.set_ylim3d([0,np.pi*1.5])

plt.show()