from manim import *
import numpy as np


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
