from manim import *
import numpy as np

class Spectre(Scene):
    super_spectre=[
        [0,0,0,0],
        [0,13,5,-30],
        [0,11,9,120],
        [1,13,9,90],
        [1,0,2,-90],
        [1,13,5,-30],
        [5,11,5,0],
        [5,1,9,60],
        [7,1,9,60]
    ]

    # from_super_tile_index, from_tile_index, from_corner_index, to_tile_index, to_corner_index, gamma
    super_spectres=[
        [0,2,8,2,8,120],
        [0,2,8,3,8,60]
    ]

    decimals=4

    def construct(self):

        alphas=[0, -60, 90, 60, 0, 60, -90, 60, 90, 60, -90, 60, 90, -60]
        direction=[1,0,0]
        focus=DOWN
        spectre_points=[]
        spectre_creation_objects=[]
        spectre_stroke_width=6

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
        self.wait(1)

        # kunstruiere Super-Kachel
        first_tile_index=1
        last_tile_index=-1
        super_tile=self.draw_super_tile(spectre_polygon, first_tile_index, last_tile_index)

        envelope_points = self.get_envelope_points(super_tile)        



        self.play(super_tile.animate.scale(0.5).shift([-1,0,0]), run_time=0.5)
        super_tiles=[super_tile]
        for super_spectre in self.super_spectres:
            from_super_tile_index, from_tile_index, from_corner_index, to_tile_index, to_corner_index, gamma = super_spectre
            # copy, translate and rotate supertile
            from_super_tile=super_tiles[from_super_tile_index]
            from_tile=from_super_tile[from_tile_index]
            from_tile_vertices=from_tile.get_vertices()
            from_corner=from_tile_vertices[from_corner_index]
            to_tile=from_super_tile[to_tile_index]
            to_tile_vertices=to_tile.get_vertices()
            to_corner=to_tile_vertices[to_corner_index]
            translation_vector=to_corner-from_corner
       
            to_super_tile=from_super_tile.copy()
            self.add(to_super_tile)
            self.play(to_super_tile.animate.shift(translation_vector), run_time=0.5)
            self.play(Rotating(to_super_tile, about_point=to_corner, radians= gamma *DEGREES, run_time=0.3))

            super_tiles.append(to_super_tile)

        self.wait(3) 

    def draw_super_tile(self, spectre_polygon, first_tile_index, last_tile_index):
        self.play(spectre_polygon.animate.scale(0.5).shift([-2,-2,0]), run_time=0.5)
        spectre_tiles=[spectre_polygon]
        for spectre in self.super_spectre[first_tile_index:last_tile_index]:
            from_tile_index, from_corner_index, to_corner_index, beta = spectre
            from_tile=spectre_tiles[from_tile_index]
            from_tile_vertices=from_tile.get_vertices()
            from_corner=from_tile_vertices[from_corner_index]
            to_corner=from_tile_vertices[to_corner_index]
            translation_vector=to_corner-from_corner

            to_tile=from_tile.copy()
            self.add(to_tile)
            self.play(to_tile.animate.shift(translation_vector), run_time=0.5)
            self.play(Rotating(to_tile, about_point=to_corner, radians= beta *DEGREES, run_time=0.3))

            spectre_tiles.append(to_tile) 
        return VGroup(*spectre_tiles)  

    def get_envelope_points(self, polygons : VGroup):
        envelope_points = self.get_rounded_points(polygons[0])
        for polygon in polygons[1 : -1]:
            rounded_polygon_points = self.get_rounded_points(polygon) 
            frequency_by_point = dict()
            for envelope_point in envelope_points:
                frequency_by_point[envelope_point] = 1
            for polygon_point in rounded_polygon_points:
                frequency_by_point[polygon_point] = frequency_by_point.setdefault(polygon_point, 0) + 1

            neighbours_by_point = dict()
            for index, envelope_point in enumerate(envelope_points):
                next_point = envelope_points[(index + 1) % len(envelope_points)]
                previous_point = envelope_points[(index - 1) % len(envelope_points)]
                neighbours_by_point[envelope_point] = neighbours_by_point.setdefault(envelope_point, set()).add(next_point).add(previous_point)
            for polygon_point in rounded_polygon_points:
                next_point = polygon_point[(index + 1) % len(rounded_polygon_points)]
                previous_point = polygon_point[(index - 1) % len(rounded_polygon_points)]
                neighbours_by_point[polygon_point] = neighbours_by_point.setdefault(polygon_point, set()).add(next_point).add(previous_point)
           

        
               
    def get_rounded_points(self, polygon : Polygon):
        return list(map(tuple, polygon.get_vertices().round(self.decimals)))

