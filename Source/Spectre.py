from manim import *

class Spectre(Scene):
    def construct(self):

        alphas=[0, -60, 90, 60, 0, 60, -90, 60, 90, 60, -90, 60, 90, -60]
        super_sperctre=[
            [0,13,5,-30],
            [0,11,9,120],
            [1,13,9,90],
            [1,0,2,-90],
            [1,13,5,-30],
            [5,11,5,0],
            [5,1,9,60],
            [7,1,9,60]
        ]
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

        print("spectre_points: " + str(spectre_points))
        spectre_polygon=Polygon(*spectre_points, color=GREY, stroke_width=spectre_stroke_width)
        spectre_polygon.set_fill(GREEN)
        spectre_polygon.set_opacity(1)
        self.play(FadeIn(spectre_polygon),FadeOut(*spectre_creation_objects), run_time=1)
        self.wait(3)

        # kunstruiere Super-Kachel
        print("spectre_polygon: " + str(spectre_polygon.points))
        spectre_tiles=[spectre_polygon]
        for spectre in super_sperctre:
            from_tile_index, from_corner_index, to_corner_index, beta = spectre
            from_tile=spectre_tiles[from_tile_index]
            from_tile_vertices=from_tile.get_vertices()
            from_corner=from_tile_vertices[from_corner_index]
            to_corner=from_tile_vertices[to_corner_index]
            print("from_corner: " + str(from_corner))
            print("to_corner: " + str(to_corner))
            translation_vector=to_corner-from_corner

            to_tile=from_tile.copy()
            self.add(to_tile)
            self.play(to_tile.animate.shift(translation_vector), run_time=0.5)
            self.play(Rotating(to_tile, about_point=to_corner, radians= beta *DEGREES, run_time=0.3))

            spectre_tiles.append(to_tile)

        self.wait(3)           
