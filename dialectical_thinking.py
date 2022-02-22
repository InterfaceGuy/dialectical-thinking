from pydeationlib.imports import *

Project(name="dialectical_thinking",
        thinker="InterfaceGuy",
        category="diverse")

class Scene01(ThreeDScene):

    CONFIG = {
        "camera_perspective": "default",
        "camera_position": (0, 0),
        "camera_zoom": 1
    }

    def construct(self):

        cylinder = Cylinder(h=0.1, p=0.4)
        circle = Circle(radius=50, color=BLUE)
        rectangle = Rectangle(b=PI / 2, height=100, width=200, color=RED)
        shapes = Group(cylinder, circle, rectangle, group_name="shapes")
        circler = Eye(scale=0.3, x=300, h=PI, color=BLUE)
        rectangler = Eye(scale=0.3, y=300, b=PI / 2, color=RED)
        creatures = Group(circler, rectangler, group_name="creatures")
        plane_circler = Axes(
            b=PI, mode="xz", draw_grid=True, draw_ticks=False, grid_color=BLUE,
            x_grid_line_distance=100, z_grid_line_distance=100, grid_line_length=5000,
            x_start=-500, x_end=2100, z_start=-2000, z_end=400)
        plane_rectangler = Axes(
            b=PI / 2, mode="xz", draw_grid=True, draw_ticks=False, grid_color=RED,
            x_grid_line_distance=100, z_grid_line_distance=100, grid_line_length=5000,
            x_start=-500, x_end=2100, z_start=-2000, z_end=400)
        planes = Group(plane_circler, plane_rectangler, group_name="planes")

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/ \
            videos/epistemology/InterfaceGuy/scene01_audio.m4a")

        self.add(shapes, creatures, planes)
        self.play(Create(cylinder), run_time=3)
        self.play(Transform(cylinder, relative=False, p=PI / 2), run_time=3)
        self.play(Create(circler, rectangler), run_time=5)
        self.wait()
        self.play(Create(plane_circler), run_time=3)
        self.play(FadeIn(circle), run_time=2)
        self.play(UnCreate(plane_circler), run_time=2)
        self.play(Create(plane_rectangler), run_time=3)
        self.play(FadeIn(rectangle), run_time=2)
        self.play(UnCreate(plane_rectangler), FadeOut(cylinder))
        self.play(FadeOut(circle, rectangle), UnCreate(circler, rectangler))
        self.finish()

class Scene02(TwoDScene):

    def construct(self):

        # helper
        path = Arc(angle=PI, h=PI, scale_x=2, scale_z=1.3)

        # shapes
        circle_radius = 50
        circle = Circle(x=-150, radius=circle_radius, color=BLUE)
        rectangle = Rectangle(
            x=150, h=PI / 2, height=100, width=200, color=RED)
        separator = Spline([(0, 0, -500), (0, 0, 500)])
        shapes = Group(circle, rectangle, separator, group_name="shapes")

        # creatures
        circler = Eye(scale=0.3, x=-400, color=BLUE)
        rectangler = Eye(scale=0.3, x=400, h=PI, color=RED)
        cylinderer = Eye(scale=0.3, color=WHITE, b=PI)
        creatures = Group(circler, rectangler, cylinderer,
                          group_name="creatures")

        # circle empiricism
        sight_lines_circle = Group(
            # upper intersecting line
            Spline([(240, 0, 0), (circle_radius / 2 **
                                  0.5 + 50, 0, circle_radius / 2**0.5)], y=1),
            # lower intersecting line
            Spline([(240, 0, 0), (circle_radius / 2 **
                                  0.5 + 50, 0, -circle_radius / 2**0.5)], y=1),
            # middle intersecting line
            Spline([(240, 0, 0), (circle_radius + 50, 0, 0)], y=1),
            group_name="sight_lines_circle"
        )
        intersection_points_circle = Group(
            # upper point
            Cross(h=PI / 4, scale=0.03, from_center=True, x=circle_radius / \
                  2**0.5 + 50, z=circle_radius / 2**0.5),
            # lower point
            Cross(h=PI / 4, scale=0.03, from_center=True, x=circle_radius / 2**0.5 + 50,
                  z=-circle_radius / 2**0.5),
            # middle point
            Cross(h=PI / 4, scale=0.03, from_center=True,
                  x=circle_radius + 50),
            group_name="intersection_points_circle", y=1
        )
        circle_empiricism = Group(
            sight_lines_circle, intersection_points_circle, x=-100, h=PI, group_name="circle_empiricism")

        # rectangle empiricism
        sight_lines_rectangle = Group(
            # upper intersecting line
            Spline([(-240, 0, 0), (-100, 0, circle_radius / 2**0.5)], y=1),
            # lower intersecting line
            Spline([(-240, 0, 0), (-100, 0, -circle_radius / 2**0.5)], y=1),
            # middle intersecting line
            Spline([(-240, 0, 0), (-100, 0, 0)], y=1),
            group_name="sight_lines_rectangle"
        )
        intersection_points_rectangle = Group(
            # upper point
            Cross(h=PI / 4, scale=0.03, from_center=True, x=- \
                  100, z=circle_radius / 2**0.5),
            # lower point
            Cross(h=PI / 4, scale=0.03, from_center=True,
                  x=-100,  z=-circle_radius / 2**0.5),
            # middle point
            Cross(h=PI / 4, scale=0.03, from_center=True,
                  x=-100),
            group_name="intersection_points_rectangle", y=1
        )
        rectangle_empiricism = Group(
            sight_lines_rectangle, intersection_points_rectangle, x=100, h=PI, group_name="rectangle_empiricism")

        # circle mathematics
        circle_axes = Axes(mode="xz", length_x=120,
                           length_z=120, draw_ticks=False, thickness=3)
        radial_line = Spline(
            [(0, 0, 0), (circle_radius / 2**0.5, 0, circle_radius / 2**0.5)])
        sin_line = Spline(
            [(0, 0, circle_radius / 2**0.5), (circle_radius / 2**0.5, 0, circle_radius / 2**0.5)][::-1], line_style="dotted")
        cos_line = Spline(
            [(circle_radius / 2**0.5, 0, 0), (circle_radius / 2**0.5, 0, circle_radius / 2**0.5)][::-1], line_style="dotted")
        sin_text = Text("sin", scale=0.15, z=circle_radius / 2**0.5, x=-8, y=1)
        cos_text = Text("cos", scale=0.15, x=circle_radius / 2**0.5, z=-8, y=1)
        circle_mathematics = Group(circle_axes,
                                   radial_line, sin_line, cos_line, sin_text, cos_text, y=2, x=-150, group_name="circle_mathematics")

        # rectangle mathematics
        angle_radius = 20
        right_angles = Group(
            Arc(radius=angle_radius, x=-100, z=-50, y=2, h=0),
            Arc(radius=angle_radius, x=100, z=-50, y=2, h=PI / 2),
            Arc(radius=angle_radius, x=100, z=50, y=2, h=PI),
            Arc(radius=angle_radius, x=-100, z=50, y=2, h=-PI / 2),
            group_name="right_angles")
        straight_lines = Group(
            Spline([(-110, 2, 50), (110, 2, 50)]),  # upper
            Spline([(-110, 2, -50), (110, 2, -50)]),  # lower
            Spline([(-100, 2, 60), (-100, 2, -60)]),  # left
            Spline([(100, 2, 60), (100, 2, -60)]),  # right
            group_name="straight_lines")
        rectangle_mathematics = Group(
            right_angles, straight_lines, h=PI / 2, x=150, group_name="rectangle_mathematics")

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene02_audio.m4a")

        self.add(shapes, creatures, circle_empiricism,
                 rectangle_empiricism, circle_mathematics, rectangle_mathematics, path)
        self.play(Create(circler, rectangler, shapes), run_time=4)
        self.wait(2)
        self.play(DrawSteady(sight_lines_rectangle,
                             sight_lines_circle, draw_speed=200))
        self.play(Glimpse(intersection_points_rectangle,
                          intersection_points_circle, rel_end_point=1 / 4), Erase(sight_lines_rectangle,
                                                                                  sight_lines_circle), run_time=1)
        self.wait(3)
        self.play(ChangeParams(self.camera, zoom=7 / 4),
                  UnCreate(circler, rectangler))
        self.play(Create(circle_axes), Create(
            radial_line, sin_line, cos_line, sin_text, cos_text), Create(rectangle_mathematics))
        self.wait()
        self.play(UnCreate(circle_axes), Erase(
            radial_line, sin_line, cos_line, sin_text, cos_text), Erase(rectangle_mathematics))
        self.play(ChangeParams(self.camera, zoom=1))
        self.wait()
        self.play(Create(cylinderer), run_time=2)
        self.play(MoveAlongSpline(cylinderer, spline=path), run_time=2)
        self.wait()
        self.play(UnCreate(cylinderer))
        self.wait()
        self.play(UnCreate(separator))
        self.play(UnCreate(circle, rectangle))
        self.finish()


class Scene03(ThreeDScene):

    CONFIG = {
        "camera_perspective": "front",
        "camera_position": (0, 0),
        "camera_zoom": 3 / 2
    }

    def construct(self):

        circle = Circle(color=BLUE, radius=50, x=-150)
        cornered_circle = Rectangle(
            color=BLUE, width=100, height=100, rounding=1, x=-200)

        rectangle = Rectangle(color=RED, width=100, height=200, x=150)
        rounded_rectangle = Rectangle(color=RED, width=100, height=200, x=200)

        shapes = Group(circle, rectangle, cornered_circle,
                       rounded_rectangle, group_name="shapes")

        # cylinder intersection
        intersection_plane = Plane(b=PI / 2, b_frozen=PI / 4, scale=2, x=1)
        intersection_cylinder = Cylinder(
            x=150, intersects_with=[intersection_plane])
        cylinder_intersections = Group(
            intersection_cylinder, intersection_plane, group_name="cylinder_intersections")

        # flip flop animation
        def flipflop(self, pause=1 / 3, n=2):
            self.play(FadeIn(rectangle), run_time=0.1)
            self.wait(pause)
            for i in range(n):
                self.play(FadeOut(rectangle), FadeIn(
                    circle), run_time=0.1)
                self.wait(pause)
                self.play(FadeIn(rectangle), FadeOut(
                    circle), run_time=0.1)
                self.wait(pause)
            self.play(FadeOut(rectangle), run_time=0.1)
            self.wait(pause)

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene03_audio.m4a", offset=1)

        self.add(shapes, cylinder_intersections)
        self.wait(2)
        flipflop(self)
        self.play(FadeIn(circle, rectangle))
        self.play(Transform(circle, rectangle, relative=False),
                  ChangeColor(circle, rectangle, color=PURPLE), run_time=2)
        self.wait(2)
        self.play(Transform(circle, x=-200), Transform(rectangle, x=200),
                  ChangeColor(circle, color=BLUE), ChangeColor(rectangle, color=RED), run_time=3)
        self.wait(2)
        self.play(FadeIn(rounded_rectangle, cornered_circle),
                  Transform(rounded_rectangle,
                            cornered_circle, relative=False),
                  ChangeParams(rounded_rectangle, cornered_circle,
                               height=150, width=100, rounding=1 / 2),
                  ChangeColor(rounded_rectangle, cornered_circle, color=PURPLE), run_time=2)
        self.play(FadeOut(circle, rectangle, rel_end_point=1 / 2),
                  Transform(rounded_rectangle, cornered_circle, x=-150),
                  Show(intersection_plane),
                  FadeIn(intersection_cylinder, rel_start_point=1 / 2), run_time=2)
        self.play(Transform(intersection_plane, h=2 * PI, x=200), run_time=3)
        self.play(FadeOut(intersection_cylinder,
                          rounded_rectangle, cornered_circle))
        self.finish()


class Scene04(ThreeDScene):

    CONFIG = {
        "camera_perspective": "front",
        "camera_position": (0, 0),
        "camera_zoom": 1
    }

    def construct(self):

        circle = Circle(color=BLUE, radius=50, z=50, x=-250)
        rectangle = Rectangle(color=RED, width=100, height=200, z=50, x=250)
        gradient = Axes(mode="x", length_x=500, z=-100)

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene04_audio.m4a", offset=1 / 2)

        self.add(circle, rectangle, gradient)
        self.wait()
        self.play(Create(circle, rectangle), run_time=2)
        self.play(Create(gradient), run_time=2)
        self.play(UnCreate(gradient, rel_end_point=3 / 4), UnCreate(
            circle, rectangle, rel_start_point=1 / 2), run_time=2)
        self.finish()


class Scene05(ThreeDScene):

    CONFIG = {
        "camera_perspective": "default",
        "camera_position": (0, 50),
        "camera_zoom": 1
    }

    def construct(self):

        # shapes
        circle = Circle(color=BLUE, radius=50, y=-300)
        rectangle = Rectangle(color=RED, h=PI / 2, p=PI / 2,
                              width=100, height=200, x=-300)
        cylinder = Cylinder(p=PI / 2)
        shapes = Group(circle, rectangle, cylinder, group_name="shapes")

        orthogonal_axes = Axes(mode="xy", x_start=0, x_end=300,
                               y_start=0, y_end=300, b=PI, draw_ticks=False)

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene05_audio.m4a")

        self.add(shapes, orthogonal_axes)
        self.wait(2)
        self.play(Create(orthogonal_axes, smoothing_right=0, rel_end_point=1 / 2),
                  Create(circle, rectangle, smoothing_left=0, rel_start_point=1 / 3), run_time=2)
        self.wait(3)
        self.play(FadeIn(cylinder))
        self.wait()
        self.play(FadeOut(cylinder),
                  UnCreate(orthogonal_axes, rel_end_point=1 /
                           2, smoothing_right=0),
                  UnCreate(circle, rectangle, rel_start_point=1 / 3, smoothing_left=0))
        self.finish()


class Scene06(ThreeDScene):

    CONFIG = {
        "camera_perspective": "default",
        "camera_position": (0, 0),
        "camera_zoom": 1
    }

    def construct(self):

        intersection_plane = Plane(
            z=1, p=PI / 2, show=True)
        intersection_cylinder = Cylinder(
            color=RED, p=PI / 2, intersects_with=[intersection_plane], contour=False, scale=2)
        intersection = Group(intersection_plane,
                             intersection_cylinder, group_name="intersection")
        cylinder = Cylinder(p=PI / 2, scale=2)
        grid = Axes(mode="xz", x=-5000, y=5000, x_start=0, x_end=4000, z_start=0, z_end=4000, grid_line_length=100000, scale=5 / 2, p=-PI / 2, draw_ticks=False,
                    draw_grid=True, grid_color=BLUE)

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene06_audio.m4a", offset=1 / 2)

        self.add(cylinder, intersection, grid)
        self.wait()
        self.play(Create(cylinder), run_time=2)
        self.play(Create(grid), run_time=3)
        self.play(FadeIn(intersection_cylinder))
        self.play(Transform(cylinder, intersection_cylinder,
                            p=2 * PI), FadeOut(cylinder), run_time=5)
        self.play(FadeOut(intersection_cylinder), UnCreate(grid), run_time=3)
        self.finish()

class Scene07(TwoDScene):

    def construct(self):

        text = self.text(Text("trans-perspectival"))

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene07_audio.m4a")

        self.wait(5 / 2)
        self.play(Write(text))
        self.wait()
        self.play(UnWrite(text))
        self.finish()

class Scene08(ThreeDScene):

    CONFIG = {
        "camera_perspective": "default",
        "camera_position": (0, 0),
        "camera_zoom": 1
    }

    def construct(self):

        cylinder = Cylinder(p=PI / 2)
        circle = Circle(radius=50, color=BLUE)
        rectangle = Rectangle(b=PI / 2, height=100, width=200, color=RED)
        shapes = Group(cylinder, circle, rectangle, group_name="shapes")
        creature = Group(Eye(scale=0.3, x=300, h=PI,
                             color=BLUE), group_name="creature")
        plane_circler = Axes(
            b=PI, mode="xz", draw_grid=True, draw_ticks=False, grid_color=BLUE, x_grid_line_distance=100, z_grid_line_distance=100, grid_line_length=5000, x_start=-500, x_end=2100, z_start=-2000, z_end=400)
        plane_rectangler = Axes(
            b=PI / 2, mode="xz", draw_grid=True, draw_ticks=False, grid_color=RED, x_grid_line_distance=100, z_grid_line_distance=100, grid_line_length=5000, x_start=-500, x_end=2100, z_start=-2000, z_end=400)
        planes = Group(plane_circler, plane_rectangler, group_name="planes")

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene08_audio.m4a")

        self.add(shapes, creature, planes)
        self.wait()
        self.play(Create(creature))
        self.play(Create(planes), FadeIn(
            rectangle, circle, rel_start_point=1 / 2), run_time=3)
        self.play(Transform(creature, b=-PI / 2), run_time=2)
        self.play(ChangeColor(creature, color=RED), run_time=2)
        self.play(UnCreate(planes), run_time=2)
        self.play(FadeIn(cylinder), Transform(
            creature, b=4 * PI), FadeOut(circle, rectangle, rel_end_point=2 / 3), ChangeColor(creature, color=WHITE, rel_end_point=1 / 4), run_time=7)
        self.play(FadeOut(cylinder), UnCreate(creature), run_time=2)
        self.finish()

class Scene09(ThreeDScene):

    CONFIG = {
        "camera_perspective": "front",
        "camera_position": (0, 0),
        "camera_zoom": 5 / 4
    }

    def construct(self):

        # shapes
        circle = Circle(color=BLUE, radius=50, x=-200, z=50)
        rectangle = Rectangle(color=RED, width=100, height=200, x=200, z=50)
        cylinder = Cylinder(h=-PI / 2, z=25, p=-PI / 4)
        shapes = Group(circle, rectangle, cylinder, group_name="shapes")

        # text
        thesis = self.text(Text("thesis", height=30, x=-200, z=-120))
        antithesis = self.text(Text("anti-thesis", height=30, x=200, z=-120))
        synthesis = self.text(Text("syn-thesis", height=30, z=-120))

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene09_audio.m4a")

        self.add(shapes)
        self.wait(2)
        self.play(Create(circle, thesis))
        self.wait(3 / 2)
        self.play(Create(rectangle, antithesis))
        self.play(Transform(circle, x=0, z=25, b=-PI / 4, relative=False, rel_start_point=1 / 4),
                  Transform(rectangle, x=0, z=25, h=PI / 2, p=PI / 4, relative=False, rel_start_point=1 / 4), UnCreate(thesis, antithesis, rel_start_point=1 / 3), run_time=3)
        self.play(FadeIn(cylinder, rel_start_point=0), FadeOut(circle,
                                                               rectangle, rel_end_point=2 / 3), Create(synthesis), run_time=1)
        self.wait()
        self.play(UnWrite(synthesis, rel_start_point=1 / 3), FadeOut(cylinder))
        self.finish()


class Scene10(ThreeDScene):

    CONFIG = {
        "camera_perspective": "front",
        "camera_position": (0, 0),
        "camera_zoom": 5 / 4
    }

    def construct(self):

        # shapes
        circle = Circle(color=BLUE, radius=50, x=-100, z=-50, scale=1 / 2)
        rectangle = Rectangle(color=RED, width=100,
                              height=200, x=100, z=-50, scale=1 / 2)
        cylinder = Cylinder(h=-PI / 2, z=100, p=-PI / 4, scale=1 / 2)
        shapes = Group(circle, rectangle, cylinder, group_name="shapes")

        # arrows
        arrow_rectangle = Connection(
            rectangle, (20, 0, -50), (0, 0, -30), cylinder, offset_start=0.15, offset_end=0.2)
        arrow_cricle = Connection(
            circle, (-20, 0, -50), (0, 0, -30), cylinder, offset_start=0.15, offset_end=0.2)
        arrows = Group(arrow_rectangle, arrow_cricle, group_name="arrows")

        # text
        dialectical_thinking = self.text(
            Text("dialectical thinking", height=30, z=-150))

        self.audio(
            "/Users/davidrug/Documents/Ataraxia/ProjectLiminality/YouTubeChannel/videos/epistemology/InterfaceGuy/scene10_audio.m4a")

        self.add(shapes, arrows)
        self.wait(1 / 2)
        self.play(Create(rectangle, circle))
        self.play(Create(arrows))
        self.play(FadeIn(cylinder))
        self.play(Create(dialectical_thinking))
        self.wait()
        self.play(UnCreate(dialectical_thinking))
        self.finish()


scene1 = Scene01(quality="default")
#scene2 = Scene02(quality="default")
#scene3 = Scene03(quality="default")
#scene4 = Scene04(quality="default")
#scene5 = Scene05(quality="default")
#scene6 = Scene06(quality="default")
#scene7 = Scene07(quality="default")
#scene8 = Scene08(quality="default")
#scene9 = Scene09(quality="default")
#scene10 = Scene10(quality="default")
