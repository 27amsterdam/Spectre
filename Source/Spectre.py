from manim import *

class Spectre(Scene):
    def construct(self):

        alphas=[0, -60, 90, 60, 0, 60, -90, 60, 90, 60, -90, 60, 90, -60]
        direction=[1,0,0]
        focus=DOWN

        text=Text("Spectre Monotile", font_size=30).move_to([0,3.5,0])
        self.add(text)
        text=Text(str(alphas), font_size=23).move_to([0,-3.5,0])
        self.add(text)
        for alpha in alphas:
            dot=Dot(focus, color=RED)
            self.add(dot)
            end_point=focus+direction
            line=Line(focus,end_point,stroke_color=RED,stroke_width=10)
            self.play(Create(line, run_time=0.5))

            if alpha != 0:
                self.play(Rotating(line, about_point=focus,radians=alpha*DEGREES,run_time=0.5))
                
            direction=line.get_end()-focus
            focus=line.get_end()
                

        self.wait(3)