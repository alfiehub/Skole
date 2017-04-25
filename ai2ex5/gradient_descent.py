from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from math import e
from random import randint

def std_logistic(w, x):
    return 1/(1+e**(-np.inner(w, x)))

def std_logistic_diff(w, x, var='w1'):
    if var == 'w1':
        return (x[0]*e**(-np.inner(w,x)))/(1+e**(-np.inner(w,x)))**2
    elif var == 'w2':
        return (x[1]*e**(-np.inner(w,x)))/(1+e**(-np.inner(w,x)))**2

def L_simple_diff(w, var):
    return 2*(std_logistic(w,[1,0])-1)*std_logistic_diff(w, [1,0], var=var)+2*std_logistic(w,[0,1])*std_logistic_diff(w, [0,1], var=var)+2*(std_logistic(w,[1,1])-1)*std_logistic_diff(w, [1,1], var=var)

def L_simple(w):
    return (std_logistic(w, [1,0])-1)**2+(std_logistic(w, [0,1]))**2+(std_logistic(w, [1,1])-1)**2

def gradient_descent(n, i):
    w = [randint(-6,6) , randint(-6,6)]
    for i in range(i):
        if abs(w[0]) > 6.1 or abs(w[1]) > 6.1:
            break
        w[0], w[1] = (w[0]-n*L_simple_diff(w, var='w1')), (w[1]-n*L_simple_diff(w, var='w2'))
    print(n, i+1, w, L_simple(w))
    return w

#gradient_descent(1, 10000)

x = np.arange(-6, 6, 0.05)
y = np.arange(-6, 6, 0.05)

xs, ys = np.meshgrid(x, y)

zs = np.array([L_simple(np.array([x,y])) for x,y in zip(np.ravel(xs), np.ravel(ys))])

# Find the minimum value of Z and where it was found
min_z = min(zs)
min_z_index = np.where(zs==min_z)
x_cord = np.ravel(xs)[min_z_index]
y_cord = np.ravel(ys)[min_z_index]
print("Minimum value of L_simple: %r @ %r, %r" % (min_z, x_cord, y_cord))


zs = zs.reshape(xs.shape)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xs, ys, zs, cmap=cm.coolwarm, linewidth=0.01, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

zs = []
#ns = [0.0001, 0.01, 0.05, 0.1, 0.5, 0.75, 1, 2, 3, 4, 5, 10] #, 15, 25, 100]
ns = [0.01, 0.05, 0.1, 0.5, 0.75, 1, 2, 3, 4, 5, 10] #, 15, 25, 100]
for n in ns:
    zs.append(L_simple(gradient_descent(n, 1000)))


plt.plot(ns, zs)

axes = plt.gca()
axes.set_ylim([0.99*min(zs),1.01*max(zs)])

plt.xlabel('n')
plt.ylabel('L_simple')
plt.title('Value of L_simple using gradient descent with value n and 100000 iterations')
plt.grid(True)
plt.show()
