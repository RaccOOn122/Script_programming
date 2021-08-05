import numpy as np
import matplotlib.pyplot as plt

def f(x,y): 
    return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(-np.pi,np.pi/2,n)
origin = 'lower'
[X,Y]=np.meshgrid(x,y)
z=f(X,Y)

assert len(z) == len(X*Y)

plt.figure()


M1=plt.contourf(X,Y,z,
             cmap='turbo',
             origin=origin,
             alpha=0.8)
M2=plt.contour(M1,
               colors='k',
               origin=origin)

plt.savefig("sp_06/Task1_fig.png")
plt.show()
