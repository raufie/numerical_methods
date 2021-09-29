from manim import *
import numpy as np
from Roots import Roots


class Anim (Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_axis_config={"numbers_to_include": np.arange(-5, 5, 1)},
            y_length=6,
            x_length=10,
            tips=False
        )
        interval = [0, 2]
        theta = 0.01

        def f(x):
            # return x**2 - 4
            # return 3*x**3 - 2*x
            return (x-1/4)**3 - x
        # lin = np.linspace(0, 5, 100)
        # y = f(lin)
        graph = ax.get_graph(f)
        t = ValueTracker(interval[0])
        t2 = ValueTracker(interval[1])

        i = ValueTracker(interval[0])
        d = Dot(ax.coords_to_point(interval[0], f(interval[0]))).set_fill(RED)
        text = Text(f"{interval[0]}, {f(interval[0])}").next_to(d, DOWN)
        it = Text("Iteration: ").to_edge(RIGHT+UP).shift(LEFT*0.5)
        num = Text("0").next_to(it, RIGHT)
        # l = Line([[lin[0], y[0]]])

        x_label = Text("value of x1,x2=").scale(
            0.5).next_to(num, DOWN).shift(LEFT*2.15)

        num.add_updater(lambda x: x.become(
            Text(str(int(i.get_value()))).next_to(it, RIGHT)
        ))
        x_1 = Text(f"(0,3)").scale(0.5).next_to(x_label, RIGHT)
        # valut tracker for x_1
        x_1.add_updater(lambda x: x.become(
            Text(f"{ '{:.2f}'.format(t.get_value())}, { '{:.2f}'.format(interval[1])}").scale(0.5).next_to(x_label, RIGHT))

        )
        d.add_updater(lambda x: x.move_to(
            [ax.coords_to_point(t.get_value(), f(t.get_value()))]))

        def text_updater(x):
            x.become(
                Text(f"{ '{:.2f}'.format(t.get_value())}, { '{:.2f}'.format(f(t.get_value()))}").scale(0.75).next_to(d, DOWN))

        text.add_updater(text_updater)

        d2 = Dot(ax.coords_to_point(
            interval[1], f(interval[1]))).set_fill(YELLOW)
        d2.add_updater(lambda x: x.move_to(
            [ax.coords_to_point(t2.get_value(), f(t2.get_value()))]))

        line_req = Line([interval[0], -2, 1],
                        [interval[1], -2, 1]).set_fill(BLUE)
        line_req.add_updater(lambda x:
                             x.become(Line([t.get_value(), -2, 1],
                                           [t2.get_value(), -2, 1]).set_fill(BLUE)))
        vert_line = Line([(interval[0]+interval[1])/2, -2, 1],
                         [(interval[0]+interval[1])/2, 2, 1]).set_fill(BLUE)
        vert_line.add_updater(lambda x:
                              x.become(Line([(t.get_value() + t2.get_value())/2, -2, 1],
                                            [(t.get_value() + t2.get_value())/2, 2, 1]).set_fill(BLUE)))
        # print(ax.i2gp(interval[0], f))
        self.play(Create(ax))
        self.add(graph, d, d2, text, it, num, x_1,
                 x_label, line_req, ax, vert_line)
        # self.play(t.animate.set_value(3))

 # BISEC
        iteration = 0
        while True:
            x1 = interval[0]
            x2 = interval[1]
            if f(x1)*f(x2) < 0:
                # divide and continue
                mid = (x1+x2) / 2
                if f(x1)*f(mid) < 0:
                    interval = [x1, mid]
                    print(i.get_value())

                    # self.play()
                    print(interval)
                elif f(mid)*f(x2) < 0:
                    print(i.get_value())

                    interval = [mid, x2]

                    print(interval)
                else:
                    print("f(x1),f(x2) both greater than 0")
            else:
                print("f(x1),f(x2) both greater than 0")

            self.play(i.animate.set_value(i.get_value()+1),
                      t.animate.set_value(interval[0]),
                      t2.animate.set_value(interval[1]),
                      run_time=0.6
                      )
            if(abs(f(x1)-f(x2)) < theta):
                print("converged")
                print("root is " + str((x1+x2)/2))
                break
            # do 11 iterations
            if iteration > 11:
                break
            iteration += 1
        t_end = Text("approx root  = " +
                     "{:.2f}".format((interval[0]+interval[1])/2)).set_fill(YELLOW).scale(2.0)
        self.wait(2)
        self.play(FadeOut(graph, d, d2, text, it, num, x_1, x_label, ax))
        self.play(Write(t_end), run_time=1)
        self.wait(2)


class Converge2Params(ThreeDScene):
    def construct(self):
        def f(x, y):
            return x**2-y**3 - 1

 # Setting up axes
        ax = ThreeDAxes(z_range=[-5, 5], y_range=[-5, 5], tips=False)
        x_label = ax.get_x_axis_label("x")
        y_label = ax.get_y_axis_label("y")
        z_label = ax.get_z_axis_label("z")

        self.add(ax, x_label, y_label, z_label)
        vg = VGroup()
        self.set_camera_orientation(theta=-75*DEGREES, phi=120*DEGREES)
 # making plane
        r = Roots(lambda x, y: x**2-y**3 - 1, [[-5, -5], [10, 10]], 0.001)

        intervals = r.apply_bisection_2_params()

        def f(x, y):
            return x**2-y**3 - 1

        def f_p(x, y):
            return np.array([x, y, x**2-y**3 - 1])
        surface = Surface(
            f_p,
            u_range=[-5, 5],
            v_range=[-5, 5],

            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),
        )
        surface.set_opacity(0.3)
        self.add(surface)
        for arr in intervals:

            x1 = arr[0][0]
            y1 = arr[0][1]
            x2 = arr[1][0]
            y2 = arr[1][1]
            # l1 = Line3D([x1, 0, 0], [x2, 0, 0])
            # l2 = Line3D([0, y1, 0], [0, y2, 0])
            l1 = Line([x1, 0, 0], [0, y1, 0])
            # l2 = Line([x1, 0, 0], [0, y2+0.00001, 0])
            # l3 = Line([x2, 0, 0], [0, y2+0.00001, 0])
            l4 = Line([x2, 0, 0], [0, y2, 0])

            vg = VGroup(l1, l4)
            self.play(Create(vg))
            self.play(FadeOut(vg))

        # print(ax.coords_to_point([-1, -1, -1]))
