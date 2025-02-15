# API Reference

gh2 implements most of Processing's APIs related to 2D, all of the supported APIs are list below. Noticed that the API reference for gh2 copies most of [Processing's API reference](https://processing.org/reference/) but replace examples and some features for gh2.

- [Color](#color)
- [Constants](#constants)
- [Helpers](#helpers)
- [Image](#image) ([CImage](#cimage), [Display](#display))
- [Environment](#environment)
- [Events](#events) ([Keyboard](#keyboard), [Mouse](#mouse), [Cursor](#cursor))
- [IO](#io)
- [Math](#math) ([CVector](#cvector), [Calculation](#calculation), [Trigonometry](#trigonometry), [Random](#random))
- [Structure](#structure)
- [Shape](#shape) ([2D Primitives](#2D-Primitives), [Attributes](#attributes), [Vertex](#vertex), [Curves](#curves))
- [Time](#time)
- [Transform](#transform)
- [Typography](#typography)

## Color

Methods for creating, reading and setting colors.

- [gh.CColor](./color.md#ccolor) - Creates colors for storing in variables of the color datatype.
- [gh.background](./color.md#background) - Sets the color used for the background of terminal.
- [gh.fill](./color.md#fill) - Sets the color used to fill shapes.
- [gh.no_fill](./color.md#no_fill) - Disables filling shapes.
- [gh.no_stroke](./color.md#no_stroke) - Disables drawing the stroke (outline).
- [gh.stroke](./color.md#stroke) - Sets the color used to draw lines and borders around shapes.
- [gh.color_mode](./color.md#color_mode) - Changes the way gh2 interprets color data.
- [gh.lerp_color](./color.md#lerp_color) - Blends two colors to find a third color somewhere between them.

## Constants

Constants for angle.

- [gh.PI](./constants.md#PI) - PI is a mathematical constant with the value 3.1415927.
- [gh.HALF_PI](./constants.md#HALF_PI) - HALF_PI is a mathematical constant with the value 1.5707964.
- [gh.QUARTER_PI](./constants.md#QUARTER_PI) - QUARTER_PI is a mathematical constant with the value 0.7853982.
- [gh.TAU](./constants.md#TAU) - TAU is a mathematical constant with the value 6.2831855.
- [gh.TWO_PI](./constants.md#TWO_PI) - TWO_PI is a mathematical constant with the value 6.2831855.
  
## Helpers

Methods for improving programming efficiency.

- [gh.print](./helpers.md#print) - Print output to file to debug.
- [gh.check_params](./helpers.md#check_params) - Checks the type of params to output the potential error.

## Image

Methods for drawing image to screen.

### CImage

Date type for gh2 to store and manipulate image.

- [gh.CImage](./image.md#cimage) - Creates a new CImage (the datatype for storing images).
- [CImage.load_pixels](./image.md#load_pixels) - Loads the pixels data for this image into the `pixels` attribute.
- [CImage.update_pixels](./image.md#update_pixels) - Updates the backing canvas for this image with the contents of the `pixels` array.
- [CImage.set](./image.md#set) - Set the color of a single pixel.
- [CImage.get](./image.md#get) - Get the color of a single pixel.

### Display

Methods for display images.

- [gh.image](./image.md#image) - Draw an image to the charming canvas.
- [gh.image_mode](./image.md#image_mode) - Set image mode.
- [gh.load_image](./image.md#load_image) - Loads an image from a path and creates a CImage from it.
- [gh.no_tint](./image.md#no_tint) - Removes the current fill value for displaying images.
- [gh.tint](./image.md#tint) - Sets the fill value for displaying images.

## Environment

Methods for set and get runtime environment.

- [gh.cursor](./environment.md#cursor) - Set the cursor visible.
- [gh.set_cursor](./environment.md#set_cursor) - Set the positions of cursor in cells.
- [gh.no_cursor](./environment.md#no_cursor) - Hide the cursor.
- [gh.frame_rate](./environment.md#frame_rate) - Specifies the number of frames to be displayed every second.
- [gh.full_screen](./environment.md#full_screen) - Sets the sketch to fill the entire terminal.
- [gh.get_frame_count](./environment.md#get_frame_count) - The system variable frame_count contains the number of frames that have been displayed since the program started.
- [gh.get_height](./environment.md#get_height) - System variable that stores the height of the drawing canvas.
- [gh.get_width](./environment.md#get_width) - System variable that stores the width of the drawing canvas.
- [gh.size](./environment.md#size) - Sets the dimensions of it in cells for the sketch.

## Events

Methods for listening and handling events.

### Keyboard

Methods for keyboard events.

- [gh.get_key](./events.md#get_key) - The system variable key always contains the value of the most recent key on the keyboard that was used (either pressed or released).
- [gh.get_key_code](./events.md#get_key_code) - The variable keyCode is used to detect special keys such as the arrow keys (UP, DOWN, LEFT, and RIGHT) as well as ENTER, SPACE.
- [gh.get_key_pressed](./events.md#get_key_pressed) - The boolean system variable key_pressed is true if any key is pressed and false if no keys are pressed.
- [gh.key_pressed](./events.md#key_pressed) - The function decorated by key_pressed decorator is called once every time a key is pressed.
- [gh.key_released](./events.md#key_released) - The function decorated by key_released decorator is called once every time a key is released.
- [gh.key_typed](./events.md#key_typed) - The function decorated by key_typed decorator is called once every time a key is typed.

### Mouse

Methods for mouse events.

- [gh.get_mouse_x](./events.md#get_mouse_x) - The system variable mouse_x always contains the current horizontal coordinate of the mouse.
- [gh.get_mouse_y](./events.md#get_mouse_y) - The system variable mouse_y always contains the current vertical coordinate of the mouse.
- [gh.get_mouse_pressed](./events.md#get_mouse_pressed) - The mouse_pressed variable stores whether or not a mouse button is currently being pressed.
- [gh.get_mouse_button](./events.md#get_mouse_button) - When a mouse button is pressed, the value of the system variable mouseButton is set to either LEFT, RIGHT, or CENTER, depending on which button is pressed.
- [gh.mouse_clicked](./events.md#mouse_clicked) - The function decorated mouse_clicked decorator is called after a mouse button has been pressed and then released.
- [gh.mouse_pressed](./events.md#mouse_pressed) - The function decorated mouse_released decorator is called after a mouse button has been pressed.
- [gh.mouse_released](./events.md#mouse_released) - The function decorated mouse_released decorator is called after a mouse button has been released.

### Cursor

Methods for cursor events.

- [gh.get_cursor_x](./events.md#get_cursor_x) - The system variable cursor_x always contains the current horizontal coordinate of the cursor.
- [gh.get_cursor_y](./events.md#get_cursor_y) - The system variable cursor_y always contains the current vertical coordinate of the cursor.
- [gh.get_pcursor_x](./events.md#get_pcursor_x) - The system variable pcursor_x always contains the horizontal position of the cursor in the frame previous to the current frame.
- [gh.get_pcursor_y](./events.md#get_pcursor_y) - The system variable pcursor_y always contains the vertical position of the cursor in the frame previous to the current frame.
- [gh.cursor_moved](./events.md#cursor_moved) - The function decorated cursor_moved decorator is called after a cursor moved.
- [gh.cursor_pressed](./events.md#cursor_pressed) - The function decorated cursor_pressed decorator is called after a cursor pressed.
- [gh.get_cursor_moved](./events.md#get_cursor_moved) - The boolean system variable cursor_moved is true if any cursor is pressed and false if cursor is not pressed.

## IO

Methods for IO.

- [gh.load_json](./io.md#load_json) - Loads data from JSON file to dict object.
- [gh.load_csv](./io.md#load_csv) - Loads data from CSV file to dict object.

## Math

Methods related to math.

### CVector

Methods for manipulation vector object which is useful for simulating physic system.

- [gh.CVector](./math.md#cvector) - A class to describe a two dimensional vector, specifically a Euclidean (also known as geometric) vector.
- [CVector.random_2D](./math.md#random_2D) - Make a new 2D unit vector with a random direction.
- [CVector.from_angle](./math.md#from_angle) - Make a new 2D unit vector from an angle.
- [cvector.set](./math.md#set) - Set the components of the vector.
- [cvector.copy](./math.md#copy) - Get a copy of the vector.
- [cvector.mag](./math.md#mag) - Calculate the magnitude of the vector.
- [cvector.mag_sq](./math.md#mag-sq) - Calculate the magnitude of the vector, squared.
- [cvector + other](./math.md#add) - Adds x and y components to a vector, one vector to another, or two independent vectors .
- [cvector - other](./math.md#sub) - Subtract x and y components from a vector, one vector from another, or two independent vectors.
- [cvector * other](./math.md#mult) - Multiply a vector by a scalar  .
- [cvector / other](./math.md#div) - Divide a vector by a scalar.
- [cvector.dist](./math.md#dist) - Calculate the distance between two points.
- [cvector.dot](./math.md#dot) - Calculate the dot product of two vectors.
- [cvector.cross](./math.md#cross) - Calculate and return the cross product.
- [cvector.normalize](./math.md#normalize) - Normalize the vector to a length of 1.
- [cvector.limit](./math.md#limit) - Limit the magnitude of the vector.
- [cvector.mag = number](./math.md#set_mag) - Set the magnitude of the vector.
- [cvector.heading](./math.md#heading) - Calculate the angle of rotation for this vector.
- [cvector.rotate](./math.md#rotate) - Rotate the vector by an angle.
- [cvector.lerp](./math.md#lerp) - Linear interpolate the vector to another vector.
- [cvector.angle_between](./math.md#angle-between) - Calculate and return the angle between two vectors.
- [cvector.array](./math.md#array) - Return a representation of the vector as a float array.

### Calculation

Methods for basic math calculation.

- [gh.abs](./math.md#abs) - Calculates the absolute value (magnitude) of a number. The absolute value of a number is always positive.
- [gh.ceil](./math.md#ceil) - Calculates the closest int value that is greater than or equal to the value of the parameter.
- [gh.constrain](./math.md#constrain) - Constrains a value to not exceed a maximum and minimum value.
- [gh.dist](./math.md#dist) - Calculates the distance between two points.
- [gh.exp](./math.md#exp) - Returns Euler's number e (2.71828...) raised to the power of the n parameter.
- [gh.floor](./math.md#floor) - Calculates the closest int value that is less than or equal to the value of the parameter.
- [gh.lerp](./math.md#lerp) - Calculates a number between two numbers at a specific increment.
- [gh.log](./math.md#log) - Calculates the natural logarithm (the base-e logarithm) of a number.
- [gh.mag](./math.md#mag) - Calculates the magnitude (or length) of a vector.
- [gh.map](./math.md#map) - Re-maps a number from one range to another.
- [gh.max](./math.md#max) - Determines the largest value in a sequence of numbers, and then returns that value.
- [gh.min](./math.md#min) - Determines the smallest value in a sequence of numbers, and then returns that value.
- [gh.norm](./math.md#norm) - Normalizes a number from another range into a value between 0 and 1.
- [gh.pow](./math.md#pow) - Facilitates exponential expressions.
- [gh.round](./math.md#round) - Calculates the integer closest to the n parameter.
- [gh.sq](./math.md#sq) - Squares a number (multiplies a number by itself).
- [gh.sqrt](./math.md#sqrt) - Calculates the square root of a number.

### Trigonometry

Methods for calculate trigonometry.

- [gh.acos](./math.md#acos) - The inverse of cos(), returns the arc cosine of a value.
- [gh.asin](./math.md#asin) - The inverse of sin(), returns the arc sine of a value.
- [gh.atan](./math.md#atan) - The inverse of tan(), returns the arc tangent of a value.
- [gh.atan2](./math.md#atan2) - Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis.
- [gh.cos](./math.md#cos) - Calculates the cosine of an angle.
- [gh.degrees](./math.md#degrees) - Converts a radian measurement to its corresponding value in degrees.
- [gh.radians](./math.md#radians) - Converts a degree measurement to its corresponding value in radians.
- [gh.sin](./math.md#sin) - Calculates the sine of an angle.
- [gh.tan](./math.md#tan) - Calculates the ratio of the sine and cosine of an angle.

### Random

Methods for generate random numbers.

- [gh.noise](./math.md#noise) - Returns the Perlin noise value at specified coordinates.
- [gh.noise_detail](./math.md#noise-detail) - Adjusts the character and level of detail produced by the Perlin noise function.
- [gh.noise_seed](./math.md#noise-seed) - Sets the seed value for noise().
- [gh.random](./math.md#random) - Generates random numbers.
- [gh.random_gaussian](./math.md#random-gaussian) - Returns a float from a random series of numbers having a mean of 0 and standard deviation of 1.
- [gh.random_seed](./math.md#random-seed) - Sets the seed value for random().

## Structure

Methods for controlling the running flow of sketch.

- [gh.setup](./structure.md#setup) - The function decorated by setup() decorator is called once when the program starts.
- [gh.draw](./structure.md#draw) - The function decorated by draw() called directly after setup(), it continuously executes the lines of code contained inside its block until the program is stopped or no_loop() is called.
- [gh.run](./structure.md#run) - Run the sketch or nothing magic will happen.
- [gh.no_loop](./structure.md#no_loop) - Stops gh2 from continuously executing the code within draw().
- [gh.loop](./structure.md#loop) - The draw() loop may be stopped by calling no_loop(). In that case, the draw() loop can be resumed with loop().
- [gh.get_is_looping](./structure.md#get_is_looping) - get_is_looping() returns the current state for use within custom event handlers.
- [gh.redraw](./structure.md#redraw) - Executes the code within draw() one time.
- [gh.push](./structure.md#push) - The push() function saves the current drawing style settings and transformations, while pop() restores these settings.
- [gh.pop](./structure.md#pop) - The push() function saves the current drawing style settings and transformations, while pop() restores these settings.
- [gh.open_context](./structure.md#open_context) - The syntactic sugar for push() and pop().
- [gh.exit](./structure.md#exit) - Exit the sketch.

## Shape

Methods for drawing shapes.

### 2D Primitives

Methods for drawing 2D basic shapes.

- [gh.arc](./shape.md#arc) - Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse defined by the a, b, c, and d parameters.
- [gh.circle](./shape.md#circle) - Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height.
- [gh.ellipse](./shape.md#ellipse) - Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle.
- [gh.line](./shape.md#line) - Draws a line (a direct path between two points) to the screen.
- [gh.point](.shape.md#point) - Draws a point, a coordinate in space at the dimension of one cell.
- [gh.quad](./shape.md#quad) - A quad is a quadrilateral, a four sided polygon.
- [gh.rect](./shape.md#rect) - Draws a rectangle to the screen. A rectangle is a four-sided shape with every angle at ninety degrees.
- [gh.square](./shape.md#square) - Draws a square to the screen.
- [gh.triangle](./shape.md#triangle) - A triangle is a plane created by connecting three points
  
### Attributes

Methods for setting drawing attributes.

- [gh.ellipse_mode](./shape.md#ellipse_mode) - Modifies the location from which ellipses are drawn by changing the way in which parameters given to ellipse() are interpreted.
- [gh.rect_mode](./shape.md#rect_mode) - Modifies the location from which rectangles are drawn by changing the way in which parameters given to rect() are interpreted.
- [gh.stroke_weight](./shape.md#stroke_weight) - Sets the width of the stroke used for lines, points, and the border around shapes.

### Vertex

Methods for drawing custom shapes.

- [gh.begin_shape](./shape.md#begin_shape) - Using the begin_shape() and end_shape() functions allow creating more complex forms.
- [gh.end_shape](./shape.md#end_shape) - The end_shape() function is the companion to begin_shape() and may only be called after beginShape().
- [gh.open_shape](./shape.md#open_shape) - The syntax sugar for begin_shape and end_shape.
- [gh.vertex](./shape.md#vertex) - All shapes are constructed by connecting a series of vertices.
- [gh.begin_contour](./shape.md#begin_contour) - Use the begin_contour() and end_contour() function to create negative shapes within shapes such as the center of the letter 'O'.
- [gh.end_contour](./shape.md#end_contour) - Use the begin_contour() and end_contour() function to create negative shapes within shapes such as the center of the letter 'O'.
- [gh.open_contour](./shape.md#open_contour) - The syntax sugar for begin_contour and end_contour.
- [gh.bezier_vertex](./shape.md#bezier_vertex) - Specifies vertex coordinates for Bezier curves.
- [gh.curve_vertex](./shape.md#curve_vertex) - Specifies vertex coordinates for curves.

### Curves

Methods for drawing curves.

- [gh.bezier](./shape.md#bezier) - Draws a Bezier curve on the screen.
- [gh.bezier_point](./shape.md#bezier_point) - Evaluates the Bezier at point t for points a, b, c, d
- [gh.bezier_tangent](./shape.md#bezier_tangent) - Calculates the tangent of a point on a Bezier curve.
- [gh.curve](./shape.md#curve) - Draws a curved line on the screen.
- [gh.curve_point](./shape.md#curve_point) - Evaluates the curve at point t for points a, b, c, d.
- [gh.curve_tangent](./shape.md#curve_tangent) - Calculates the tangent of a point on a curve. 
- [gh.curve_tightness](./shape.md#curve_tightness) - Modifies the quality of forms created with curve() and curveVertex().

## Time

Methods for returning information about current time.

- [gh.day](./time.md#day) - The day() function returns the current day as a value from 1 - 31.
- [gh.hour](./time.md#hour) - The hour() function returns the current hour as a value from 0 - 23.
- [gh.millis](./time.md#millis) - Returns the number of milliseconds (thousandths of a second) since starting the program.
- [gh.minute](./time.md#minute) - The minute() function returns the current minute as a value from 0 - 59.
- [gh.month](./time.md#month) - The month() function returns the current month as a value from 1 - 12.
- [gh.second](./time.md#second) - The second() function returns the current second as a value from 0 - 59.
- [gh.year](./time.md#year) - The year() function returns the current year as an integer (2003, 2004, 2005, etc).

## Transform

Methods for applying transformations to objects.

- [gh.translate](./transform.md#translate) - Specifies an amount to displace objects within the display window.
- [gh.scale](./transform.md#scale) - Increases or decreases the size of a shape by expanding or contracting vertices.
- [gh.rotate](./transform.md#rotate) - Rotates a shape by the amount specified by the angle parameter.
- [gh.shear_x](./transform.md#shear_x) - Shears a shape around the x-axis by the amount specified by the angle parameter.
- [gh.shear_y](./transform.md#shear_y) Shears a shape around the y-axis by the amount specified by the angle parameter.

## Typography

Methods for drawing expected text to screen.

- [gh.text](./typography.md#text) - Draws text to the screen.
- [gh.text_width](./typography.md#text_width) - Calculates and returns the width of any character or text string.
- [gh.text_align](./typography.md#text_align) - Sets the current alignment for drawing text.
- [gh.text_size](./typography.md#text_size) - Sets the current font size.
- [gh.text_height](./typography.md#text_height) - Calculates and returns the height of any character or text string.
- [gh.get_font_list](./typography.md#get_font_list) - Returns the supported font list for text with BIG font size.
- [gh.text_font](./typography.md#text_font) - Sets the current font that will be drawn with the text() function.
