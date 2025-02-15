# Structure

<a name="setup" href="#setup">#</a> gh.**setup**(*foo*)

The function decorated by setup() decorator is called once when the program starts. It's used to define initial environment properties such as screen size and background color and to load media such as images as the program starts.

```py
import gh2 as gh


a = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.background('O')
    gh.fill('+', gh.YELLOW, gh.CYAN)
    gh.no_stroke()


@gh.draw
def draw():
    global a
    gh.rect(a % gh.get_width(), 2, 2, gh.get_height() - 4)
    a += 1


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_setup.gif" />

<a name="draw" href="#draw">#</a> gh.**draw**(*foo*)

The function decorated by draw() called directly after setup(), it continuously executes the lines of code contained inside its block until the program is stopped or no_loop() is called. Note if no_loop() is called in setup(), draw() will still be executed once before stopping. draw() is called automatically and should never be called explicitly.

```py
import gh2 as gh

y = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.frame_rate(10)


@gh.draw
def draw():
    global y
    gh.background(' ')
    gh.line(0, y, gh.get_width(), y)
    y = (y + 1) % gh.get_height()


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_draw.gif" />

<a name="run" href="#run">#</a> gh.**run**()

Run the sketch or nothing magic will happen.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

gh.rect(0, 0, 5, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_run.png" />

<a name="no_loop" href="#no_loop">#</a> gh.**no_loop**()

Stops gh2 from continuously executing the code within draw(). If loop() is called, the code in draw() begins to run continuously again. If using no_loop() in setup(), it should be the last line inside the block.

<a name="loop" href="#loop">#</a> gh.**loop**()

By default, gh2 loops through draw() continuously, executing the code within it. However, the draw() loop may be stopped by calling no_loop(). In that case, the draw() loop can be resumed with loop().

<a name="get_is_looping" href="#get_is_looping">#</a> gh.**get_is_looping**()

```py
import gh2 as gh

y = 0

@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.frame_rate(10)


@gh.draw
def draw():
    global y
    gh.background(' ')
    gh.line(0, y, gh.get_width(), y)
    y = (y + 1) % gh.get_height()


@gh.mouse_clicked
def mouse_clicked():
    if gh.get_is_looping():
        gh.no_loop()
    else:
        gh.loop()


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_loop.gif" />

<a name="redraw" href="#redraw">#</a> gh.**redraw**()

Executes the code within draw() one time. This function allows the program to update the display window only when necessary, for example when an event registered by mouse_pressed() or key_pressed() occurs.

```py
import gh2 as gh

x = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.no_loop()


@gh.draw
def draw():
    global x
    gh.background(' ')
    gh.line(x, 0, x, gh.get_height())
    x = (x + 1) % gh.get_width()


@gh.mouse_clicked
def mouse_clicked():
    gh.redraw()


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_redraw.gif" />

<a name="push" href="#push">#</a> gh.**push**() <br/>
<a name="pop" href="#pop">#</a> gh.**pop**()

The push() function saves the current drawing style settings and transformations, while pop() restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with push(), it builds on the current style and transform information.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

gh.ellipse(5, 5, 10, 5)

gh.push()
gh.fill('+', gh.YELLOW, gh.CYAN)
gh.stroke('O', gh.BLUE, gh.GREEN)
gh.translate(15, 0)
gh.ellipse(5, 5, 10, 5)
gh.pop()

gh.ellipse(35, 5, 10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_push.png" />

<a name="open_context" href="#open_context">#</a> gh.**open_context**()

The syntactic sugar for push() and pop().

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

gh.ellipse(5, 5, 10, 5)

with gh.open_context():
  gh.fill('+', gh.YELLOW, gh.CYAN)
  gh.stroke('O', gh.BLUE, gh.GREEN)
  gh.translate(15, 0)
  gh.ellipse(5, 5, 10, 5)

gh.ellipse(35, 5, 10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_push.png" />

<a name="exit" href="#exit">#</a> gh.**exit**()

Exit the sketch.

```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.color_mode(gh.RGB)


@gh.draw
def draw():
    b = gh.get_frame_count() % 255
    color = (0, 0, b)
    gh.background(' ', color, color)


@gh.mouse_clicked
def mouse_clicked():
    gh.exit()


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_exit.gif" />
