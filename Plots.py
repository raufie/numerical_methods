import matplotlib.pyplot as plt
import numpy as np


def getSurface(f):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    print(x)
    print(y)
    z = f(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    [t.set_color('white') for t in ax.xaxis.get_ticklabels()]
    [t.set_color('white') for t in ax.yaxis.get_ticklabels()]
    [t.set_color('white') for t in ax.zaxis.get_ticklabels()]
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.zaxis.label.set_color("white")
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    plt.savefig("plt.png", transparent=True)


def f(x, y):

    return 4*x**2 - 2*x


getSurface(f)
