import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

def f(x, y, t): return 0.5*np.sin(x**3) + 0.25*np.sin((y - t)**2)

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(0,np.pi*1.5,n)

res = [[f(xx, yy, 0) for xx in x] for yy in y]

X,Y = np.meshgrid(x,y)

fig, ax = plt.subplots(figsize=(10,7))

ax.set_xlim(-np.pi/2,np.pi/2)
ax.set_ylim(0,np.pi*1.5)



M1=plt.contourf(X,Y,z,
             cmap='turbo',
             alpha=0.8)
M2=plt.contour(M1,
               colors='k')


def animate(i):
    ax.clear()
    z=f(X,Y,i)
    ax.contourf(M1[:,:,z])
    return ax

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=False) 
plt.show()