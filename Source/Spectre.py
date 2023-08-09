from manim import *

class Spectre(Scene):
    def construct(self):

        alphas=[0, -60, 90, 60, 0, 60, -90, 60, 90, 60, -90, 60, 90, -60]
        direction=[1,0,0]
        focus=DOWN
        spectre_points=[]
        spectre_creation_objects=[]
        spectre_stroke_width=10

        text=Text("Spectre Monotile", font_size=30).move_to([0,3.5,0])
        self.add(text)
        text=Text(str(alphas), font_size=23).move_to([0,-3.5,0])
        self.add(text)
        for alpha in alphas:
            dot=Dot(focus, color=RED)
            self.add(dot)
            spectre_creation_objects.append(dot)
            end_point=focus+direction
            line=Line(focus,end_point,stroke_color=RED,stroke_width=spectre_stroke_width)
            self.play(Create(line, run_time=0.5))
            spectre_creation_objects.append(line)

            if alpha != 0:
                self.play(Rotating(line, about_point=focus,radians=alpha*DEGREES,run_time=0.5))
                
            direction=line.get_end()-focus
            focus=line.get_end()  
            spectre_points.append(focus)             

        spectre_polygon=Polygon(*spectre_points, color=GREY, stroke_width=spectre_stroke_width)
        spectre_polygon.set_fill(GREEN)
        spectre_polygon.set_opacity(1)
        self.play(FadeIn(spectre_polygon),FadeOut(*spectre_creation_objects), run_time=1)
        self.wait(3)
