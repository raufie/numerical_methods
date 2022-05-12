import matplotlib.pyplot as plt
import numpy as np
import random

x_values = [float(x) for x in input("input x values").split(" ")]
y_values = [float(x) for x in input("input y values").split(" ")]
x_values_i = x_values[:]
y_values_i = y_values[:]


xmax = np.max(x_values_i)+2.
xmin = np.min(x_values_i)-2.
ymax = np.max(y_values_i)+2.

ymin = np.min(y_values_i)-2.


def get_random_hex():
    def r():
        return random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


colors = []


def get_f(x_values, y_values, x):
    cummulative_f = 0
    distributions = []
    for i, y in enumerate(y_values):
        L_n = y
        for j, xj in enumerate(x_values):
            if i != j:
                # distributions.append(((x-xj))/(x_values[i] - xj))
                L_n *= ((x-xj))/(x_values[i] - xj)
        cummulative_f += L_n
        distributions.append(L_n)
    return cummulative_f, distributions


if len(x_values) != len(y_values):

    exit()
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color=['red'])

x_space = np.linspace(np.min(x_values), np.max(x_values), 100)
y_pred = [get_f(x_values, y_values, x)[0] for x in x_space]
ax.scatter(x_space, y_pred, color=['green'], s=5)


coords = []


def onclick(event):
    if event.dblclick:
        new_x = event.xdata
        new_y = event.ydata
        x_values.append(new_x)
        y_values.append(new_y)
        # print(new_x, new_y)
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))

        plt.clf()
        ax.set(xlim=(-100, 100), ylim=(-100, 100))

        plt.scatter(x_values, y_values, color=['red'])
        plt.draw()
        x_space = np.linspace(np.min(x_values)-2., np.max(x_values)+2., 4000)
        x_space_short = np.linspace(
            np.min(x_values)-2., np.max(x_values)+2., 500)
        y_pred = [get_f(x_values, y_values, x)[0] for x in x_space]
        constitutes = [get_f(x_values, y_values, x)[1] for x in x_space_short]
        colors.append(get_random_hex())

        # for i in range(len(constitutes[0])):
        #     y_c = [c[i] for c in constitutes]
        #     colors.append(get_random_hex())
        #     plt.scatter(x_space_short, y_c, color=[colors[i]], s=1, alpha=0.2)

        print(len(x_values))

        plt.scatter(x_space, y_pred, color=['green'], s=5)

        ax.set(xlim=(-100, 100), ylim=(-100, 100))
        plt.axis([-100, 100, -100, 100])
        plt.draw()


plt.axis('tight')
plt.autoscale(False)

ax.set(xlim=(-100, 100), ylim=(-100, 100))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
plt.draw()
