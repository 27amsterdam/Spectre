from manim import *

class Spectre(Scene):
    def construct(self):

        alphas=[0.5, 0.5, 1, 1, 1.5, 1.5, 2, 2, 2.5, 2.5, 3, 3]
        direction=[1.0,0.0,0.0]
        focus=DOWN

        text=Text("Snail :)", font_size=30).move_to([0,3.5,0])
        self.add(text)
        for alpha in alphas:
            dot=Dot(focus, color=RED)
            self.add(dot)
            end_point=focus+[x*alpha for x in direction]
            line=Line(focus,end_point,stroke_color=RED,stroke_width=10)
            self.play(Create(line, run_time=0.5))
            self.play(Rotating(line, about_point=focus,radians=90*DEGREES,run_time=0.5))
                
            direction=(line.get_end()-focus)/alpha
            focus=line.get_end()
        

                

        self.wait(3)