# Color

Methods for creating, reading and setting colors.

<a name="ccolor" href="#ccolor">#</a> gh.**CColor**(*ch*=" "[, *fg*[, *bg*]]) : CColor

Creates colors for storing in variables of the color data type. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

c0 = gh.CColor()
c1 = gh.CColor('@')
c2 = gh.CColor('@', gh.RED)
c3 = gh.CColor('@', gh.RED, gh.YELLOW)

gh.stroke(c0)
gh.point(0, 0) # nothing

gh.stroke(c1)
gh.point(1, 1) # ('@', gh.WHITE, gh.BLACK)

gh.stroke(c2)
gh.point(2, 2) # ('@', gh.RED, gh.BLACK)

gh.stroke(c3)
gh.point(3, 3) # ('@', gh.RED, gh.YELLOW)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ccolor.png" width="100%"/>

<a name="background" href="#background">#</a> gh.**background**(*ch*=" "[, *fg*[, *bg*]])<br>
<a name="background" href="#background">#</a> gh.**background**(*ccolor*)

Sets the color used for the background of terminal. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

This function is typically used within draw() to clear the display window at the beginning of each frame, but it can be used inside setup() to set the background on the first frame of animation or if the background need only be set once.

```py
import lighght as gh


@gh.setup
def setup():
    c = gh.CColor('*')
    gh.full_screen()
    gh.frame_rate(2)
    gh.no_cursor()
    gh.background(c)  # use CColor


x = 0


@gh.draw
def draw():
    global x
    x += 1
    t = gh.get_frame_count() % 3

    if t == 0:
        gh.background('@')  # one channel
    elif t == 1:
        gh.background('+', gh.BLUE)  # two channel
    else:
        gh.background('-', gh.RED, gh.BLUE)  # three channel


    gh.fill('0', gh.YELLOW, gh.RED)
    gh.stroke('1', gh.GREEN, gh.BLUE)
    gh.rect(0, 0, 5, 5)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_background.gif" width="100%"/>

<a name="fill" href="#fill">#</a> gh.**fill**(*ch*=" "[, *fg*[, *bg*]])<br/>
<a name="fill" href="#fill">#</a> gh.**fill**(*ccolor*)

Sets the color used to fill shapes. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.fill('@', gh.RED, gh.BLUE)
gh.rect(0, 0, 10, 5)

gh.fill('O', gh.YELLOW, gh.CYAN)
gh.rect(20, 0, 10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_fill.png" width="100%"/>

<a name="no_fill" href="#no_fill">#</a> gh.**no_fill**()

Disables filling shapes. If both `no_stroke()` and `no_fill()` are called, nothing will be drawn to the screen.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.fill('@', gh.RED, gh.BLUE)
gh.rect(0, 0, 10, 5)

gh.no_fill()
gh.rect(20, 0, 10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_fill.png" width="100%"/>

<a name="no_stroke" href="#no_stroke">#</a> gh.**no_stroke**()

Disables drawing the stroke (outline). If both `no_stroke()` and `no_fill()` are called, nothing will be drawn to the screen.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.fill('@', gh.RED, gh.BLUE)
gh.rect(0, 0, 10, 5)

gh.no_stroke()
gh.rect(20, 0, 10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_stroke.png" width="100%"/>

<a name="stroke" href="#stroke">#</a> gh.**stroke**(*ch*="*"[, *fg*[, *bg*]])<br/>
<a name="stroke" href="#stroke">#</a> gh.**stroke**(*ccolor*)

Sets the color used to draw lines and borders around shapes. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.RED, gh.BLUE)
gh.rect(0, 0, 10, 5)

gh.stroke('O', gh.YELLOW, gh.CYAN)
gh.rect(20, 0, 10, 5)

gh.run()
```

<a name="color_mode" href="#color_mode">#</a> gh.**color_mode**(*mode*=ANSI | RGB | HSB[, *max1*[, *max2*, [, *max3*]]])

color_mode() changes the way Lighght interprets color data. By default, the parameters for fill(), stroke(), background(), and color() are defined by values between 0 and 255 using ANSI color.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

for i in range(256):
    x = i % 32
    y = i // 32
    gh.stroke(' ', i, i)
    gh.point(x, y)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_ansi_256.png" width="100%"/>

To make it easier to use ANSI color, there are some predefined constants which can be used directly as below.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

# basic colors
colors = [
    gh.RED,
    gh.BLACK,
    gh.CYAN,
    gh.YELLOW,
    gh.GREEN,
    gh.BLUE,
    gh.WHITE,
    gh.MAGENTA
]

gh.stroke_weight(1)
for i, c in enumerate(colors):
    x = 5
    y = 2
    gh.stroke("@", c, c)
    gh.point(i * 5 + x , y)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_ansi_baisc.png" width="100%"/>

Setting `color_mode(HSB)` lets you use the HSB system instead. In this situation, each color is represented by three-elements tuple `(hue, saturation, brightness)`. The hue channel is between 0 and 255, and the saturation or brightness channel is between 0 and 100. It is useful to draw a rainbow.

```py
import lighght as gh

gh.full_screen()
gh.color_mode(gh.HSB)
gh.no_cursor()


# rainbows
w = 30
h = 360 / w

for hue in range(360):
    i = hue % w
    j = hue // w
    gh.stroke(" ", (hue, 100, 100), (hue, 100, 100))
    gh.point(i, j)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_hsb.png" width="100%"/>

Setting `color_mode(RGB)` lets you use the HSB system instead. In this situation, each color is represented by three-elements tuple `(red, green, blue)`. The red, green, blue channels are all between 0 and 255. `(c,)` is short for `(c, c, c)`. It can be used to draw color with only one channel.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.color_mode(gh.RGB)

n = 7
gh.stroke_weight(1)

for i in range(n):
    c = gh.map(i, 0, n, 0, 255)
    gh.stroke(" ", (c, 0, 0), (c, 0, 0))
    gh.point(i * 5 + 5, 2)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_rgb_red.png" width="100%"/>

It also can be used to draw gray colors.

```py
import lighght as gh

gh.full_screen()
gh.color_mode(gh.RGB)
gh.no_cursor()

n = 7
gh.stroke_weight(1)

for i in range(n):
    c = gh.map(i, 0, n, 0, 255)
    gh.stroke("@", (c,), (c,))
    gh.point(i * 5 + 5, 2)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_rgb_gray.png" width="100%"/>

<a name="lerp_color" href="#lerp_color">#</a> gh.**lerp_color**(*start*, *stop*, *amt*)

Blends two colors to find a third color somewhere between them. The amt parameter is the amount to interpolate between the two values where 0.0 equal to the first color, 0.1 is very near the first color, 0.5 is halfway in between, etc.

Noticed that not only does it interpolate color `bg` and `fg`, it also will interpolates `ch` as well.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

start = gh.CColor('a', gh.BLUE, gh.RED)  # start color
end = gh.CColor('z', gh.GREEN, gh.YELLOW)  # end color

gh.stroke_weight(1)
n = 10
for i in range(n):
    t = i / n
    c = gh.lerp_color(start, end, t)
    gh.stroke(c)
    gh.point(i * 5 + 5, 2)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_lerp_color_ansi.png" width="100%"/>

It also can be used to interpolate color in RGB and HSB color mode.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.color_mode(gh.RGB)

start = gh.CColor('a', (0,), (255, 0, 0))
end = gh.CColor('z', (255, 255, 0), (0,))
n = 10

for i in range(n):
    t = i / n
    c = gh.lerp_color(start, end, t)
    gh.stroke_weight(1)
    gh.stroke(c)
    gh.point(i * 5 + 5, 2)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_lerp_color_rgb.png" width="100%"/>