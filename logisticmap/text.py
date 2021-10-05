from manim import *


class Anim(Scene):
    def construct(self):

        ax = Axes(x_range=[2.0, 5, 1], y_range=[0, 1, 1])
   # g = ax.get_graph()
        self.add(ax)
        color = PINK
        d = Dot().set_fill(color).set_opacity(0.5).scale(0.5).move_to(
            ax.coords_to_point(2.7, 0.5))
        self.play(Create(d, run_time=0.000008))
        d2 = Dot().set_fill(color).set_opacity(0.5).scale(0.5).move_to(
            ax.coords_to_point(2.8, 0.7))
        self.play(Create(d2, run_time=0.000008))
        d3 = Dot().set_fill(color).set_opacity(0.5).scale(0.5).move_to(
            ax.coords_to_point(2.7, 0.9))
        self.play(Create(d3, run_time=0.000008))
        d4 = Dot().set_fill(color).set_opacity(0.5).scale(0.5).move_to(
            ax.coords_to_point(3.7, 0.9))
        self.play(Create(d4, run_time=0.000008))
        self.wait()
