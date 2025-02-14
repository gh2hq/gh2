# Shape

Methods for drawing shapes.

## 2D Primitives

Methods for drawing 2D basic shapes.

<a name="arc" href="#arc">#</a> gh.**arc**(*a*, *b*, *c*, *d*, *start*, *stop*, *mode=OPEN | CHORD | PIE*)

Draw an arc to the screen. If called with only x, y, w, h, start and stop, the arc will be drawn and filled as an open pie segment. If a mode parameter is provided, the arc will be filled like an open semi-circle (OPEN), a closed semi-circle (CHORD), or as a closed pie segment (PIE). The origin may be changed with the ellipseMode() function.The arc is always drawn clockwise from wherever start falls to wherever stop falls on the ellipse.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.arc(12, 5, 20, 10, 0, gh.PI + gh.QUARTER_PI, gh.OPEN)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_arc_open.png" width="100%"/>

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.arc(12, 5, 20, 10, 0, gh.PI + gh.QUARTER_PI, gh.PIE)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_arc_pie.png" width="100%"/>

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.arc(12, 5, 20, 10, 0, gh.PI + gh.QUARTER_PI, gh.CHORD)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_arc_chord.png" width="100%"/>

<a name="circle" href="#circle">#</a> gh.**circle**(*x*, *y*, *extend*)

Draws a circle to the screen. A circle is a simple closed shape. It is the set of all points in a plane that are at a given distance from a given point, the centre. This function is a special case of the ellipse() function, where the width and height of the ellipse are the same. Height and width of the ellipse correspond to the diameter of the circle. By default, the first two parameters set the location of the centre of the circle, the third sets the diameter of the circle.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.circle(12, 6, 10)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_circle.png" width="100%"/>

<a name="ellipse" href="#ellipse">#</a> gh.**ellipse**(*a*, *b*, *c*, *d*)

Draws an ellipse (oval) to the screen. By default, the first two parameters set the location of the center of the ellipse, and the third and fourth parameters set the shape's width and height. If no height is specified, the value of width is used for both the width and height. If a negative height or width is specified, the absolute value is taken.

An ellipse with equal width and height is a circle. The origin may be changed with the ellipse_mode() function.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.ellipse(12, 6, 20, 10)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ellipse.png" width="100%"/>

<a name="line" href="#line">#</a> gh.**line**(*x1*, *y1*, *x2*, *y2*)

Draws a line (a direct path between two points) to the screen. This width can be modified by using the stroke_weight() function. A line cannot be filled, therefore the fill() function will not affect the color of a line. So to color a line, use the stroke() function.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.line(1, 1, 10, 10)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_line.png" width="100%"/>

<a name="point" href="#point">#</a> gh.**point**(*x*, *y*)

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.point(5, 5)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_point.png" width="100%"/>

<a name="quad" href="#quad">#</a> gh.**quad**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*)

Draws a quad on the canvas. A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.quad(
    9, 0,  # point1
    27 + 5, 2,  # point2
    19, 12,  # point3
    9, 7  # point4
)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_quad.png" width="100%"/>

<a name="rect" href="#rect">#</a> gh.**rect**(*a*, *b*, *c*, *d*)

Draws a rectangle on the canvas. A rectangle is a four-sided closed shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, may be changed with the rect_mode() function.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.rect(1, 1, 10, 10)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rect.png" width="100%"/>

<a name="square" href="#square">#</a> gh.**square**(*x*, *y*, *extend*)

Draws a square to the screen. A square is a four-sided shape with every angle at ninety degrees, and equal side size. This function is a special case of the rect() function, where the width and height are the same, and the parameter is called "s" for side size. By default, the first two parameters set the location of the upper-left corner, the third sets the side size of the square. The way these parameters are interpreted, may be changed with the rect_mode() function.


```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.square(1, 1, 10)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_square.png" width="100%"/>

<a name="triangle" href="#triangle">#</a> gh.**square**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*)

Draws a triangle to the canvas. A triangle is a plane created by connecting three points. The first two arguments specify the first point, the middle two arguments specify the second point, and the last two arguments specify the third point.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.triangle(
    6, 0,  # point1
    12, 6,  # point2
    0, 6 # point3
)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_triangle.png" width="100%"/>

## Attributes

Methods for setting drawing attributes.

<a name="ellipse_mode" href="#ellipse_mode">#</a> gh.**ellipse_mode**(*mode=CENTER | RADIUS | CORNER | CORNERS*)

Modifies the location from which ellipses are drawn by changing the way in which parameters given to ellipse(), circle() and arc() are interpreted.

The default mode is CENTER, in which the first two parameters are interpreted as the shape's center point's x and y coordinates respectively, while the third and fourth parameters are its width and height.

ellipse_mode(RADIUS) also uses the first two parameters as the shape's center point's x and y coordinates, but uses the third and fourth parameters to specify half of the shape's width and height.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer  ellipse
gh.fill('O', gh.RED, gh.YELLOW)
gh.ellipse_mode(gh.RADIUS) 
gh.ellipse(12, 6, 20, 10)

# Inner ellipse
gh.fill('V', gh.BLUE, gh.GREEN)
gh.ellipse_mode(gh.CENTER)
gh.ellipse(12, 6, 20, 10)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ellipse_mode_center.png" width="100%"/>

ellipse_mode(CORNER) interprets the first two parameters as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

ellipse_mode(CORNERS) interprets the first two parameters as the location of one corner of the ellipse's bounding box, and the third and fourth parameters as the location of the opposite corner.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer  ellipse
gh.fill('O', gh.RED, gh.YELLOW)
gh.ellipse_mode(gh.CORNER) 
gh.ellipse(8, 4, 16, 8)

# Inner ellipse
gh.fill('V', gh.BLUE, gh.GREEN)
gh.ellipse_mode(gh.CORNERS)
gh.ellipse(8, 4, 16, 8)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ellipse_mode_corner.png" width="100%"/>

<a name="rect_mode" href="#rect_mode">#</a> gh.**rect_mode**(*mode=CENTER | RADIUS | CORNER | CORNERS*)

Modifies the location from which rectangles are drawn by changing the way in which parameters given to rect() are interpreted.

The default mode is CORNER, which interprets the first two parameters as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

rect_mode(CORNERS) interprets the first two parameters as the location of one of the corners, and the third and fourth parameters as the location of the diagonally opposite corner. Note, the rectangle is drawn between the coordinates, so it is not necessary that the first corner be the upper left corner.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer rect
gh.fill('O', gh.RED, gh.YELLOW)
gh.rect_mode(gh.CORNER) 
gh.rect(8, 4, 16, 8)

# Inner rect
gh.fill('V', gh.BLUE, gh.GREEN)
gh.rect_mode(gh.CORNERS)
gh.rect(8, 4, 16, 8)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rect_mode_corner.png" width="100%"/>

rect_mode(CENTER) interprets the first two parameters as the shape's center point, while the third and fourth parameters are its width and height.

rect_mode(RADIUS) also uses the first two parameters as the shape's center point, but uses the third and fourth parameters to specify half of the shape's width and height respectively.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer  rect
gh.fill('O', gh.RED, gh.YELLOW)
gh.rect_mode(gh.RADIUS) 
gh.rect(12, 6, 10, 5)

# Inner rect
gh.fill('V', gh.BLUE, gh.GREEN)
gh.rect_mode(gh.CENTER)
gh.rect(12, 6, 10, 5)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rect_mode_center.png" width="100%"/>

<a name="stroke_weight" href="#stroke_weight">#</a> gh.**stroke_weight**(*weight=0*)

Sets the width of the stroke used for lines, points and the border around shapes. All widths are set in units of cells.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke_weight(0) # Default
gh.stroke('O')
gh.line(3, 0, 25, 0)

gh.stroke('A')
gh.stroke_weight(1) # Thicker
gh.line(3, 3, 25, 3)

gh.stroke('X')
gh.stroke_weight(2) # Beastly
gh.line(3, 8, 25, 8)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_stroke_weight.png" width="100%"/>

## Vertex

Methods for drawing custom shapes.

<a name="begin_shape" href="#begin_shape">#</a> gh.**begin_shape**(*primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN | QUADS | QUAD_STRIP*)

Using the begin_shape() and end_shape() functions allow creating more complex forms. begin_shape() begins recording vertices for a shape and end_shape() stops recording. The value of the kind parameter tells it which types of shapes to create from the provided vertices. With no mode specified, the shape can be any irregular polygon.

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape()
gh.vertex(1, 1)
gh.vertex(6, 1)
gh.vertex(6, 6)
gh.vertex(1, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_polygon.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.LINES)
gh.vertex(1, 1)
gh.vertex(6, 1)
gh.vertex(6, 6)
gh.vertex(1, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_lines.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.POINTS)
gh.vertex(1, 1)
gh.vertex(6, 1)
gh.vertex(6, 6)
gh.vertex(1, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_points.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.TRIANGLES)
gh.vertex(1, 6)
gh.vertex(5, 1)
gh.vertex(10, 6)
gh.vertex(15, 1)
gh.vertex(20, 6)
gh.vertex(25, 1)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_triangles.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.TRIANGLE_STRIP)
gh.vertex(1, 6)
gh.vertex(5, 1)
gh.vertex(10, 6)
gh.vertex(15, 1)
gh.vertex(20, 6)
gh.vertex(25, 1)
gh.vertex(30, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_triangle_strip.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.TRIANGLE_FAN)
gh.vertex(11, 6)
gh.vertex(11, 1)
gh.vertex(21, 6)
gh.vertex(11, 11)
gh.vertex(1, 6)
gh.vertex(11, 1)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_triangle_fan.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.QUADS)
gh.vertex(1, 1)
gh.vertex(1, 6)
gh.vertex(6, 6)
gh.vertex(6, 1)
gh.vertex(11, 1)
gh.vertex(11, 6)
gh.vertex(16, 6)
gh.vertex(16, 1)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_quads.png" width="100%"/>

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.QUAD_STRIP)
gh.vertex(1, 1)
gh.vertex(1, 6)
gh.vertex(6, 1)
gh.vertex(6, 6)
gh.vertex(11, 1)
gh.vertex(11, 6)
gh.vertex(16, 1)
gh.vertex(16, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_quad_strip.png" width="100%"/>

<a name="end_shape" href="#end_shape">#</a> gh.**end_shape**(*mode=OPEN | CLOSE*)

The end_shape() function is the companion to begin_shape() and may only be called after begin_shape(). When endShape() is called, all of image data defined since the previous call to begin_shape() is written into the image buffer. The constant CLOSE as the value for the MODE parameter to close the shape (to connect the beginning and the end).

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape()
gh.vertex(1, 1)
gh.vertex(6, 1)
gh.vertex(1, 6)
gh.end_shape()

gh.begin_shape()
gh.vertex(8, 1)
gh.vertex(13, 1)
gh.vertex(8, 6)
gh.end_shape(gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_end_shape.png" width="100%"/>

<a name="vertex" href="#vertex">#</a> gh.**vertex**(*x*, *y*)

All shapes are constructed by connecting a series of vertices. vertex() is used to specify the vertex coordinates for points, lines, triangles, quads, and polygons. It is used exclusively within the begin_shape() and end_shape() functions.

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape()
gh.vertex(1, 1)
gh.vertex(6, 1)
gh.vertex(6, 6)
gh.vertex(1, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_polygon.png" width="100%"/>

<a name="open_shape" href="#open_shape">#</a> gh.**open_shape**(*primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN, mode=OPEN | CLOSE*)

The syntactic sugar for begin_shape() and end_shape().

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

with gh.open_shape(gh.LINES, gh.CLOSE):
    gh.vertex(1, 1)
    gh.vertex(6, 1)
    gh.vertex(6, 6)
    gh.vertex(1, 6)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_open_shape.png" width="100%"/>

<a name="begin_contour" href="#begin_contour">#</a> gh.**begin_contour**()
<a name="end_contour" href="#end_contour">#</a> gh.**end_contour**()

Use the begin_contour() and end_contour() functions to create negative shapes within shapes such as the center of the letter 'O'. beginContour() begins recording vertices for the shape and endContour() stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior clockwise order, then for internal shapes, draw vertices shape in counter-clockwise.

These functions can only be used within a begin_shape()/end_shape() pair and transformations such as translate(), rotate(), and scale() do not work within a begin_contour()/end_contour() pair. It is also not possible to use other shapes, such as ellipse() or rect() within.

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# Outer shape
gh.begin_shape()

gh.vertex(0, 0)
gh.vertex(15, 0)
gh.vertex(15, 15)
gh.vertex(0, 15)

# Inner shape
gh.begin_contour()
gh.vertex(5, 5)
gh.vertex(5, 10)
gh.vertex(10, 10)
gh.vertex(10, 5)
gh.end_contour()

gh.end_shape(gh.CLOSE)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_contour.png" width="100%"/>

<a name="open_contour" href="#open_contour">#</a> gh.**open_contour**()

The syntactic sugar for begin_contour() and end_contour().

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# Shapes
gh.begin_shape()
with gh.open_shape(close_mode=gh.CLOSE):
  gh.vertex(0, 0)
  gh.vertex(15, 0)
  gh.vertex(15, 15)
  gh.vertex(0, 15)
  with gh.open_contour():
    gh.vertex(5, 5)
    gh.vertex(5, 10)
    gh.vertex(10, 10)
    gh.vertex(10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_open_contour.png" width="100%"/>

<a name="bezier_vertex" href="#bezier_vertex">#</a> gh.**bezier_vertex**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*)

Specifies vertex coordinates for Bezier curves. Each call to bezier_vertex() defines the position of two control points and one anchor point of a Bezier curve, adding a new segment to a line or shape.

The first time bezier_vertex() is used within a begin_shape() call, it must be prefaced with a call to vertex() to set the first anchor point. This function must be used between begin_shape() and end_shape() and only when there is no MODE or POINTS parameter specified to begin_shape().

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom curve
with gh.open_shape():
    gh.vertex(30, 5)
    gh.bezier_vertex(80, 0, 80, 35, 30, 35)
    gh.bezier_vertex(50, 30, 60, 25, 30, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_bezier_vertex.png" width="100%"/>

<a name="curve_vertex" href="#curve_vertex">#</a> gh.**bezier_vertex**(*x*, *y*)

Specifies vertex coordinates for curves. This function may only be used between begin_shape() and end_shape() and only when there is no MODE parameter specified to begin_shape().

The first and last points in a series of curve_vertex() lines will be used to guide the beginning and end of a the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with curve_vertex() will draw the curve between the second, third, and fourth points. The curve_vertex() function is an implementation of Catmull-Rom splines.

```py
import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom curve
with gh.open_shape():
    gh.curve_vertex(44, 21)
    gh.curve_vertex(44, 21)
    gh.curve_vertex(48, 9)
    gh.curve_vertex(21, 7)
    gh.curve_vertex(2, 30)
    gh.curve_vertex(2, 30)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_curve_vertex.png" width="100%"/>

## Curves

Methods for drawing curves.

<a name="bezier" href="#bezier">#</a> gh.**bezier**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*)

Draws a cubic Bezier curve on the screen. These curves are defined by a series of anchor and control points. The first two parameters specify the first anchor point and the last two parameters specify the other anchor point, which become the first and last points on the curve. The middle parameters specify the two control points which define the shape of the curve. Approximately speaking, control points "pull" the curve towards them.

Bezier curves were developed by French automotive engineer Pierre Bezier, and are commonly used in computer graphics to define gently sloping curves. See also curve().

<a name="bezier_point" href="#bezier_point">#</a> gh.**bezier_point**(*n1*, *n2*, *n3*, *n4*, *t*)

Given the x or y co-ordinate values of control and anchor points of a bezier curve, it evaluates the x or y coordinate of the bezier at position t. The parameters a and d are the x or y coordinates of first and last points on the curve while b and c are of the control points.The final parameter t is the position of the resultant point which is given between 0 and 1. This can be done once with the x coordinates and a second time with the y coordinates to get the location of a bezier curve at t.

<a name="bezier_tangent" href="#bezier_tangent">#</a> gh.**bezier_tangent**(*n1*, *n2*, *n3*, *n4*, *t*)

Evaluates the tangent to the Bezier at position t for points a, b, c, d. The parameters a and d are the first and last points on the curve, and b and c are the control points. The final parameter t varies between 0 and 1.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.YELLOW, gh.RED)
gh.fill('+', gh.GREEN, gh.BLUE)

# only a bezier curve
with gh.open_context():
    gh.no_fill()
    gh.bezier(40, 5, 10, 10, 50, 20, 10, 30)

# a bezier curve with points
t = 0
cnt = 4
gh.translate(20, 0)
with gh.open_context():
    gh.no_fill()
    gh.bezier(40, 5, 10, 10, 50, 20, 10, 30)

    gh.stroke('a', gh.RED, gh.YELLOW)
    gh.stroke_weight(1)
    while t <= 1:
        x = gh.bezier_point(40, 10, 50, 10, t)
        y = gh.bezier_point(5, 10, 20, 30, t)
        gh.point(x, y)
        t += 1 / cnt

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_bezier.png" width="100%"/>

<a name="curve" href="#curve">#</a> gh.**curve**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*)

Draws a curved line on the screen between two points, given as the middle four parameters. The first two parameters are a control point, as if the curve came from this point even though it's not drawn. The last two parameters similarly describe the other control point.

Longer curves can be created by putting a series of curve() functions together or using curveVertex(). An additional function called curveTightness() provides control for the visual quality of the curve. The curve() function is an implementation of Catmull-Rom splines.

<a name="curve_tangent" href="#curve_tangent">#</a> gh.**curve_tangent**(*n1*, *n2*, *n3*, *n4*, *t*)

Evaluates the tangent to the curve at position t for points a, b, c, d. The parameter t varies between 0 and 1, a and d are points on the curve, and b and c are the control points.

<a name="curve_tightness" href="#curve_tightness">#</a> gh.**curve_tangent**(*v*)

Modifies the quality of forms created with curve() and curve_vertex().The parameter tightness determines how the curve fits to the vertex points. The value 0.0 is the default value for tightness (this value defines the curves to be Catmull-Rom splines) and the value 1.0 connects all the points with straight lines. Values within the range -5.0 and 5.0 will deform the curves but will leave them recognizable and as values increase in magnitude, they will continue to deform.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.YELLOW, gh.RED)
gh.fill('+', gh.GREEN, gh.BLUE)

# A curve with tightness of 1
with gh.open_context():
    gh.curve_tightness(1)
    gh.no_fill()
    gh.curve(-55, 26, 13, 24, 13, 11, -45, 25)

# A curve with tightness of 0
with gh.open_context():
    gh.translate(20, 0)
    gh.curve_tightness(0)  # default
    gh.no_fill()
    gh.curve(-55, 26, 13, 24, 13, 11, -45, 25)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_curve_tightness.png" width="100%"/>

<a name="curve_point" href="#curve_point">#</a> gh.**curve_point**(*n1*, *n2*, *n3*, *n4*, *t*)

Evaluates the curve at position t for points a, b, c, d. The parameter t varies between 0 and 1, a and d are control points of the curve, and b and c are the start and end points of the curve. This can be done once with the x coordinates and a second time with the y coordinates to get the location of a curve at t.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.YELLOW, gh.RED)
gh.fill('+', gh.GREEN, gh.BLUE)

# A curve with some points
with gh.open_context():
    gh.no_fill()
    gh.curve(-55, 26, 13, 24, 13, 11, -45, 25)

    t = 0
    cnt = 3
    gh.stroke('p', gh.CYAN, gh.RED)
    gh.stroke_weight(1)
    while t <= 1:
        x = gh.curve_point(-55, 13, 13, -45, t)
        y = gh.curve_point(26, 24, 11, 25, t)
        gh.point(x, y)
        t += 1 / cnt


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_curve.png" width="100%"/>