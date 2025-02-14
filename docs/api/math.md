# Math

Methods related to math.

## CVector

Methods for manipulation vector object which is useful for simulating physic system.

<a name="cvector" href="#cvector">#</a> gh.**CVector**(*x*=0, *y*=0) : *CVector*

A class to describe a two dimensional vector, specifically a Euclidean (also known as geometric) vector.

```py
from lighght import CVector

v1 = CVector() 
v2 = CVector(1, 2)

v1 # (0, 0)
v2 # (1, 2)
```

<a name="set" href="#set">#</a> cvector.**set**(*x*=0", *y*=0) : *CVector* <br/>
<a name="set" href="#set">#</a> cvector.**set**(*vector*) : *CVector* <br/>
<a name="set" href="#set">#</a> cvector.**set**(*list*) : *CVector* <br/>

Set the components of the vector.

```py
from lighght import CVector

v = CVector()
v.set(1, 2) # (1, 2)

v1 = CVector()
v1.set(v) # (1, 2)
v1.set([2, 3]) # (2, 3)
```

<a name="random_2D" href="#random_2D">#</a> CVector.**random_2D**() : *CVector*

Make a new 2D unit vector with a random direction.

```py
from lighght import CVector
from math import isclose

v = CVector.random_2D()
isclose(v.mag, 1.0) # true
```

<a name="from_angle" href="#from_angle">#</a> CVector.**from_angle**() : *CVector*

Make a new 2D unit vector from an angle.

```py
from lighght import CVector
from math import pi, isclose

v = CVector.from_angle(math.pi / 3)
isclose(v.mag, 1.0) # true
```

<a name="copy" href="#copy">#</a> cvector.**copy**() : *CVector*

Get a copy of the vector.

```py
from lighght import CVector

v = CVector(1, 2)
v1 = v.copy() # (1, 2)
```

<a name="mag" href="#mag">#</a> cvector.**mag**() : *number*

Calculate the magnitude of the vector.

```py
from lighght import CVector

v = CVector(3, 4)
v.mag # 5.0
```

<a name="mag_sq" href="#mag_sq">#</a> cvector.**mag_sq**() : *number*

Calculate the magnitude of the vector, squared.

```py
from lighght import CVector

v = CVector(3, 4)
v.mag_sq() # 25
```

<a name="add" href="#add">#</a> cvector *+* other : *CVector*

Adds x and y components to a vector, one vector to another, or two independent vectors.

```py
import lighght as gh

v1 = gh.CVector(1, 2)
v2 = gh.CVector(3, 4)
v1 + v2 # (4, 6)
v1 += v2 # (4, 6)
```

<a name="sub" href="#sub">#</a> cvector *-* other : *CVector*

Subtract x and y components from a vector, one vector from another, or two independent vectors.

```py
from lighght import CVector

v1 = CVector(4, 2)
v2 = CVector(2, 1)
v1 - v2 # (2, 1)
v1 -= v2 # (2, 1)
```

<a name="mul" href="#mul">#</a> cvector <i>*</i> other : <i>CVector</i>

Multiply a vector by a scalar.

```py
from lighght import CVector

v =CVector(2, 3)
v * 2 # (4, 6)
2 * v # (4, 6)
-v # (-2, -3)
v *= 2 #(4, 6)
```

<a name="div" href="#div">#</a> cvector */* other: *CVector*

Divide a vector by a scalar.

```py
from lighght import CVector

v = CVector(2, 4)
v / 2 # (1.0, 2.0)
v /= 2 # (1.0, 2.0)
```

<a name="dist" href="#dist">#</a> cvector.**dist**(*cvector*) : *number*

Calculate the distance between two points.

```py
from lighght import CVector

v1 = CVector(1, 2)
v2 = CVector(4, 6)
v1.dist(v2) # 5.0
```

<a name="dot" href="#dot">#</a> cvector.**dot**(*cvector*) : *number*

Calculate the dot product of two vectors.

```py
from lighght import CVector

v1 = CVector(1, 2)
v2 = CVector(2, 3)
v1.dot(v2) # 8
```

<a name="cross" href="#cross">#</a> cvector.**cross**(*cvector*) : *number*

Calculate and return the cross product.

```py
from lighght import CVector

v1 = CVector(1, 2)
v2 = CVector(2, 3)
v1.cross(v2) # -1
```

<a name="normalize" href="#normalize">#</a> cvector.**normalize**() : *CVector*

Normalize the vector to a length of 1.

```py
from lighght import CVector
from math import isclose

v = CVector(3, 4)
isclose(v.normalize().mag, 1.0) # True
```

<a name="limit" href="#limit">#</a> cvector.**limit**(*max_len*) : *CVector*

Limit the magnitude of the vector.

```py
from lighght import CVector

v = CVector(3, 4)
v.limit(6).mag # 5.0
v.limit(4).mag # 4.0
```

<a name="set_mag" href="#set_mag">#</a> cvector.mag **=** *number* : *CVector*

Set the magnitude of the vector.

```py
from lighght import CVector
from math import isclose

v = CVector(3, 4)
v.mag = 2
isclose(v.mag, 2) # True
```

<a name="heading" href="#heading">#</a> cvector.**heading**(*max_len*) : *number*

Calculate the angle of rotation for this vector.

```py
from lighght import CVector
from math import pi, isclose

v = CVector(1, 1)
isclose(v.heading(), pi / 4) # True
```

<a name="rotate" href="#rotate">#</a> cvector.**rotate**(*theta*) : *CVector*

Rotate the vector by an angle (2D only)

```py
from lighght import CVector
from math import pi, isclose

v = CVector(1, 1)
isclose(v.rotate(pi / 2).heading(), pi / 4 + pi / 2) # True
```

<a name="lerp" href="#lerp">#</a> cvector.**lerp**(*cvector*, *amt*) : *CVector*

Linear interpolate the vector to another vector.

```py
from lighght import CVector
from math import isclose

v1 = CVector(1, 2)
v2 = CVector(2, 3)
v3 = v1.lerp(v2, 0.4)

isclose(v3.x, 1.4) # True
isclose(v3.y, 2.4) # True
```

<a name="angle_between" href="#angle_between">#</a> cvector.**angle_between**(*cvector*) : *number*

Calculate and return the angle between two vectors.

```py
from lighght import CVector
from math import pi, isclose

v1 = CVector.from_angle(pi / 4)
v2 = CVector.from_angle(pi / 3)
angle = v1.angle_between(v2)
isclose(angle, pi / 3 - pi / 4) # True
```

<a name="array" href="#array">#</a> cvector.**array**() : *list*

Return a representation of the vector as a float array.

```py
from lighght import CVector

v = CVector(1, 2)
v.array() # [1, 2]
```

## Calculation

Methods for basic math calculation.

<a name="abs" href="#abs">#</a> gh.**abs**(*n*) : *number*

Calculates the absolute value (magnitude) of a number.

```py
from lighght import abs

abs(1) # 1
abs(-1) # 1
abs(0) # 0
```

<a name="ceil" href="#ceil">#</a> gh.**ceil**(*n*) : *number*

Calculates the closest int value that is greater than or equal to the value of the parameter.

```py
from lighght import ceil

ceil(1.2) # 2
ceil(-1.2) # -1
ceil(1) # 1
ceil(-1) # -1
```

<a name="constrain" href="#constrain">#</a> gh.**constrain**(*amt*, *low*, *high*) : *number*

Constrains a value to not exceed a maximum and minimum value.

```py
from lighght import constrain

constrain(-1, 2, 3) # 2
constrain(4, 2, 3) # 3
constrain(2.5, 2, 3) # 2.5
```

<a name="dist" href="#dist">#</a> gh.**dist**(*x*1, *y1*, *x2*, *y2*) : *number*

Calculates the distance between two points.

```py
from lighght import dist

dist(0, 0, 1, 0) # 1.0
dist(-1, -1, 2, 3) # 5.0
```

<a name="exp" href="#exp">#</a> gh.**exp**(*n*) : *number*

Returns Euler's number e (2.71828...) raised to the power of the n parameter.

```py
from lighght import exp

exp(1) # 2.718281828459045
```

<a name="floor" href="#floor">#</a> gh.**floor**(*n*) : *number*

Calculates the closest int value that is less than or equal to the value of the parameter.

```py
from lighght import floor

floor(1.2) # 1
floor(-1.2) # -2
floor(0) # 0
```

<a name="lerp" href="#lerp">#</a> gh.**lerp**(*start*, *stop*, *amt*) : *number*

Calculates a number between two numbers at a specific increment.

```py
from lighght import lerp

lerp(1, 2, 0) # 1
lerp(1, 2, 1) # 2
lerp(10, 20, 0.2) # 12.0
```

<a name="log" href="#log">#</a> gh.**log**(*n*) : *number*

Calculates the natural logarithm (the base-e logarithm) of a number.

```py
from lighght import log

log(math.e) # 1.0
```

<a name="mag" href="#mag">#</a> gh.**mag**(*a*, *b*, *c*=0) : *number*

Calculates the magnitude (or length) of a vector.

```py
from lighght import mag

mag(3, 4) # 5.0
mag(3, 4, 12) # 13.0
```

<a name="map" href="#map">#</a> gh.**map**(*value*, *start1*, *stop1*, *start2*, *stop2*) : *number*

Re-maps a number from one range to another.

```py
from lighght import map

map(1.5, 1, 2, 10, 20) # 15
```

<a name="max" href="#max">#</a> gh.**max(*\*args*, *\*\*kw*)** : *number*

Determines the largest value in a sequence of numbers, and then returns that value.

```py
from lighght import max

max(0, 1) # 1
max(0, 1, 2) # 2
max([0, 1, 2, 3]) # 3
```

<a name="min" href="#min">#</a> gh.**max(*\*args*, *\*\*kw*)** : *number*

Determines the smallest value in a sequence of numbers, and then returns that value.

```py
from lighght import min

min(0, 1) # 0
min(0, 1, 2) # 0
min([0, 1, 2, 3]) # 0
```

<a name="norm" href="#norm">#</a> gh.**norm**(*value*, *start*, *stop*) : *number*

Normalizes a number from another range into a value between 0 and 1.

```py
from lighght import norm

norm(20, 0, 50) # 0.4
```

<a name="pow" href="#pow">#</a> gh.**pow**(*n*, *e*) : *number*

Facilitates exponential expressions.

```py
from lighght import pow

pow(3, 2) # 9.0
pow(4, 0.5) # 2.0
```

<a name="round" href="#round">#</a> gh.**round**(*n*) : *number*

Calculates the integer closest to the n parameter.

```py
from lighght import round

round(9.2) # 9
round(9.4) # 9
round(9.5) # 10
round(-1.4) # -1
round(-1.5) # -2
```

<a name="sq" href="#sq">#</a> gh.**sq**(*n*) : *number*

Squares a number (multiplies a number by itself).

```py
from lighght import sq

sq(5) # 25
```

<a name="sqrt" href="#sqrt">#</a> gh.**sqrt**(*n*) : *number*

Calculates the square root of a number.

```py
from lighght import sqrt

sqrt(25) # 5.0
```

## Trigonometry

Methods for calculate trigonometry.

<a name="acos" href="#acos">#</a> gh.**acos**(*n*) : *number*

The inverse of cos(), returns the arc cosine of a value.

```py
from lighght import acos

acos(0.5) # math.pi / 3
```

<a name="asin" href="#asin">#</a> gh.**asin**(*n*) : *number*

The inverse of sin(), returns the arc sine of a value.

```py
from lighght import asin

acos(1) # math.pi / 2
```

<a name="atan" href="#atan">#</a> gh.**atan**(*n*) : *number*

The inverse of tan(), returns the arc tangent of a value.

```py
from lighght import atan

atan(1) # math.pi / 4
```

<a name="atan2" href="#atan2">#</a> gh.**atan2**(*y*, *x*) : *number*

Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis.

```py
from lighght import atan2

atan2(1, 1) # math.pi / 4
```

<a name="cos" href="#cos">#</a> gh.**cos**(*n*) : *number*

Calculates the cosine of an angle.

```py
from lighght import cos
from lighght import PI

cos(PI / 3) # 0.5
```

<a name="degrees" href="#degrees">#</a> gh.**degrees**(*n*) : *number*

Converts a radian measurement to its corresponding value in degrees.

```py
from lighght import degrees
from lighght import PI

degrees(PI) # 180.0
```

<a name="radians" href="#radians">#</a> gh.**degrees**(*n*) : *number*

Converts a degree measurement to its corresponding value in radians.

```py
from lighght import radians

radians(180.0) # math.pi
```

<a name="sin" href="#sin">#</a> gh.**sin**(*n*) : *number*

Calculates the sine of an angle.

```py
from lighght import sin
from lighght import PI

sin(PI / 6) # 0.5
```

<a name="tan" href="#tan">#</a> gh.**tan**(*n*) : *number*

Calculates the ratio of the sine and cosine of an angle

```py
from lighght import tan
from lighght import PI

tan(PI / 4) # 1
```

## Random

Methods for generate random numbers.

<a name="noise" href="#noise">#</a> gh.**noise**(*x*, *y=0*, *z=0*) : *number*

Returns the Perlin noise value at specified coordinates.Perlin noise is a random sequence generator producing a more naturally ordered, harmonic succession of numbers compared to the standard random() function.

It was invented by Ken Perlin in the 1980s and been used since in graphical applications to produce procedural textures, natural motion, shapes, terrains etc.

The resulting value will always be between 0.0 and 1.0. The noise value can be animated by moving through the noise space as demonstrated in the example above. As a general rule the smaller the difference between inputs, the smoother the resulting noise sequence will be.

```py
import lighght as gh


xoff = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    global xoff
    gh.background(' ')
    xoff += 0.01
    n = gh.noise(xoff) * gh.get_width()
    gh.line(n, 0, n, gh.get_height())


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_noise.gif" width="100%"/>

<a name="noise_detail" href="#noise_detail">#</a> gh.**noise_detail**(*octaves=4*, *falloff=0.5*)

Adjusts the character and level of detail produced by the Perlin noise function. Similar to harmonics in physics, noise is computed over several octaves. Lower octaves contribute more to the output signal and as such define the overall intensity of the noise, whereas higher octaves create finer grained details in the noise sequence. By default, noise is computed over 4 octaves with each octave contributing exactly half than its predecessor, starting at 50% strength for the 1st octave. This falloff amount can be changed by adding an additional function parameter. Eg. a falloff factor of 0.75 means each octave will now have 75% impact (25% less) of the previous lower octave. Any value between 0.0 and 1.0 is valid, however note that values greater than 0.5 might result in greater than 1.0 values returned by noise(). By changing these parameters, the signal created by the noise() function can be adapted to fit very specific needs and characteristics.

```py
import lighght as gh


gh.full_screen()
gh.color_mode(gh.RGB)
gh.no_cursor()

gh.background(' ')
for j in range(gh.get_height()):
    for i in range(gh.get_width()):
        mid = gh.ceil(gh.get_width() / 2)
        dist = gh.abs(i - mid)
        noise_scale = 0.02
        if i < mid:
            gh.noise_detail(2, 0.2)
        else:
            gh.noise_detail(8, 0.65)
        v = gh.noise(dist * noise_scale, j * noise_scale)
        c = gh.map(v, 0, 1, 0, 255)
        gh.stroke(' ', (c,), (c,))
        gh.point(i, j)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_noise_detail.png" width="100%"/>

<a name="noise_seed" href="#noise_seed">#</a> gh.**noise_seed**(*seed*)

Sets the seed value for noise(). By default, noise() produces different results each time the program is run. Set the value parameter to a constant to return the same pseudo-random numbers each time the software is run.

```py
import lighght as gh


xoff = 0.0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.noise_seed(99)


@gh.draw
def draw():
    gh.background(' ')
    global xoff
    xoff += .01
    n = gh.noise(xoff) * gh.get_width()
    gh.line(n, 0, n, gh.get_height())


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_noise_seed.gif" width="100%"/>

<a name="random" href="#random">#</a> gh.**noise_seed**(*low*[, *high*])

Return a random floating-point number.

Takes either 0, 1 or 2 arguments.

If no argument is given, returns a random number from 0 up to (but not including) 1.

If one argument is given and it is a number, returns a random number from 0 up to (but not including) the number.

If two arguments are given, returns a random number from the first argument up to (but not including) the second argument.

```py
import lighght as gh


bar_width = 5
bar_count = 0
bars = []


@gh.setup
def setup():
    global bars, bar_count
    gh.full_screen()
    gh.no_cursor()
    bar_count = gh.floor(gh.get_width() / bar_width)
    bars = [0 for _ in range(bar_count)]


@gh.draw
def draw():
    global bars
    i = int(gh.random(bar_count))
    bars[i] += 1

    gh.background(' ')
    gh.fill('Q')
    gh.no_stroke()

    for index, bar_height in enumerate(bars):
        gh.rect(
            bar_width * index,
            gh.get_height() - bar_height,
            bar_width,
            bar_height
        )


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_random.gif" width="100%"/>

<a name="random_gaussian" href="#random_gaussian">#</a> gh.**random_gaussian**()

Returns a random number fitting a Gaussian, or normal, distribution. There is theoretically no minimum or maximum value that random_gaussian() might return. Rather, there is just a very low probability that values far from the mean will be returned; and a higher probability that numbers near the mean will be returned. Takes either 0, 1 or 2 arguments.

If no args, returns a mean of 0 and standard deviation of 1.

If one arg, that arg is the mean (standard deviation is 1).

If two args, first is mean, second is standard deviation.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

for y in range(gh.get_height()):
  mid = gh.get_width() / 2
  x = gh.random_gaussian(mid, 40)
  gh.stroke('$')
  gh.line(mid, y, x, y)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_random_gaussian.png" width="100%"/>

<a name="random_seed" href="#random_seed">#</a> gh.**random_seed**(*seed*)

Sets the seed value for random().

By default, random() produces different results each time the program is run. Set the seed parameter to a constant to return the same pseudo-random numbers each time the software is run.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.color_mode(gh.RGB)

gh.random_seed(99)
for i in range(gh.get_width()):
    r = gh.random(0, 255)
    gh.stroke(' ', (r,), (r, ))
    gh.line(i, 0, i, gh.get_height())

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_random_seed.png" width="100%"/>
