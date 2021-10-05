from manim import *
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os


class LogisticMap:
    def __init__(self, mu_min, mu_max, transient_iterations, data_iterations):
        self.mu_min = mu_min
        self.mu_max = mu_max
        self.n_trans = transient_iterations
        self.n_data = data_iterations
        # automatically iteratiing
        n_mu = 500
        self.n_mu = 500
        self.mu = np.linspace(2.4, 4, n_mu)
        self.x_data = np.zeros(shape=(self.n_data, n_mu))

        x_0 = 0.5
        # print(self.x_data.shape)

        for index, mu_i in enumerate(self.mu):
            # for every mu we must iterate to converge ti get rid of transient data(x vals)
            x = x_0  # every iteration starts with x_0
            for i in range(self.n_trans):
                x = x * mu_i * (1 - x)

            # running iterations for collecting data
            # in chaos this will give us a (lot of different data as it becomes unstable [|f'(x)| > 1]
            # and gives us period increasing 2 times and then chaos)
            for j in range(self.n_data):
                x = x*mu_i * (1-x)
                self.x_data[j][index] = x

        # print(self.x_data)


class Anim(Scene):
    def construct(self):
        l = LogisticMap(2.4, 4, 20000, 5)
        ax = Axes(x_range=[2.0, 5, 1], y_range=[0, 1, 1])
        # g = ax.get_graph()
        self.add(ax)

        for i, m in enumerate(l.mu):

            q = l.x_data[:, i]

            def get_perc(a, p1,  p2):
                # print(a)
                a = np.array(a)
                return len(a[(a > p1) & (a < p2)])/len(a)
            perc = [get_perc(q, 0, 0.2), get_perc(q, 0.2, 0.4),
                    get_perc(q, 0.4, 0.6), get_perc(q, .6, 0.8), get_perc(q, 0.8, 1.0)]
            # print(perc)

            mx = np.argmax(perc)
            color = WHITE
            if perc[mx] >= 0.8:
                color = RED
            elif perc[mx] >= 0.6:
                color = ORANGE
            elif perc[mx] >= 0.4:
                color = BLUE
            elif perc[mx] >= 0.2:
                color = GREEN
            else:
                color = WHITE
            for j in range(l.n_data):
                s = time.time()

                # loop in bins
                # more values in a bin more hot color
                # cold color for less values

                d = Dot().set_fill(color).set_opacity(0.5).scale(0.5).move_to(
                    ax.coords_to_point(l.mu[i], l.x_data[j][i]))

                self.play(Create(d, run_time=0.000008))
                # self.add(d)
                # print(v)
                # self.add(Dot().move_to(ax.coords_to_point(2.7, 0.5)))
                # print(l.)
                est_t = time.time()-s
                os.system("cls")
                t_max = 5
                print(((((i)*t_max)+j) / (t_max*500)) * 100, "%")
                print("Time Elapsed on prev anim(seconds): ", est_t)
                print("Estimated Time left based on prev anim (MINUTES)=",
                      ((len(range(l.n_data))-j)*est_t + (t_max*est_t*(len(l.mu)-i)))/60)
                print("Estimated Time left based on prev anim (HOURS)=",
                      ((len(range(l.n_data))-j)*est_t + (t_max*est_t*(len(l.mu)-i)))/3600)
            # print(np.std(l.x_data[:, i]))
        self.wait(2)
        # print(l.x_data.shape)
