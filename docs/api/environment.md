# Environment

Methods for set and get runtime environment.

<a name="cursor" href="#cursor">#</a> gh.**cursor**()

Set the cursor visible.

<a name="set_cursor" href="#set_cursor">#</a> gh.**set_cursor**(*x*, *y*)

Set the positions of cursor in cells.

```py
import lighght as gh

gh.full_screen()
gh.cursor()
gh.set_cursor(gh.get_width() / 2, gh.get_height() / 2)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_cursor.png" />

<a name="no_cursor" href="#no_cursor">#</a> gh.**no_cursor**()

Hide the cursor.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_cursor.png" />

<a name="frame_rate" href="#frame_rate">#</a> gh.**frame_rate**(*rate*)

Specifies the number of frames to be displayed every second. For example, the function call frameRate(30) will attempt to refresh 30 times a second. If the processor is not fast enough to maintain the specified rate, the frame rate will not be achieved. Setting the frame rate within setup() is recommended.

<a name="get_frame_count" href="#get_frame_count">#</a> gh.**get_frame_count**() : *number*

The system variable frameCount contains the number of frames that have been displayed since the program started.

```py
import lighght as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.frame_rate(1)


@gh.draw
def draw():
    gh.background(' ')
    gh.text_size(gh.BIG)
    gh.text_align(gh.CENTER, gh.MIDDLE)
    gh.text(gh.get_frame_count(), gh.get_width() / 2, gh.get_height() / 2)


gh.run()

```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_frame_rate.gif" />

<a name="full_screen" href="#full_screen">#</a> gh.**full_screen**(*mode=SINGLE | DOUBLE*)

Sets the sketch to fill the entire terminal.

The default mode is single mode which means render each character with only one cell. It works fine with character which take only one cell such as 'A', ';', etc.

```py
import lighght as gh

x = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    global x
    gh.background(' ')
    gh.rect(x, 0, 10, 10)
    x += 1


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_full_screen_single.gif" />

The double render mode will use two cells to render a shape character. If a character is two-cell width (💘, 🌈, etc.), it only render once while one-cell width character (a, ;, etc.) will be render twice.

In some case, Lighght cant not get the right width for characters, you can use a tuple (ch, width) to specify the width of character to avoid unexpected mess.

In double mode, a text character will still use one cell to render for one-cell width.

```py
import lighght as gh



chars = ['💘', '🌈', ('⏰', 2), '🧚', '爱', 'a']
texts = [
    'hello world',
    '🚀🚀h',
    'h🚀llo'
]

x = 0


@gh.setup
def setup():
    gh.full_screen(gh.DOUBLE)
    gh.frame_rate(2)
    gh.no_cursor()


@gh.draw
def draw():
    global x
    size = 5
    ch = chars[gh.get_frame_count() % len(chars)]
    y = 10
    x += 2

    gh.background(" ")
    gh.no_stroke()
    gh.fill(ch)

    # polygon
    gh.begin_shape()
    gh.vertex(x, y)
    gh.vertex(x + size, y)
    gh.vertex(x + size, y - size)
    gh.vertex(x + size * 2, y)
    gh.vertex(x, y + size * 2)
    gh.end_shape(gh.CLOSE)

    # text
    gh.stroke()
    for i, t in enumerate(texts):
        gh.text(t, 0, i)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_full_screen_double.gif" />

<a name="get_height" href="#get_height">#</a> gh.**get_height**() : *number*

System variable that stores the height of the drawing canvas.

<a name="get_width" href="#get_width">#</a> gh.**get_width**() : *number*

System variable that stores the width of the drawing canvas.

```py
import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.point(gh.get_width() / 2, gh.get_height() / 2)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_dimensions.png" />

<a name="size" href="#size">#</a> gh.**get_width**(*width*, *height*, *mode=SINGLE | DOUBLE*)

Sets the dimensions of it in cells for the sketch.

The default mode is single mode which means render each character with only one cell. It works fine with character which take only one cell such as 'A', ';', etc.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_size_single.gif" />

The double render mode will use two cells to render a shape character. If a character is two-cell width (💘, 🌈, etc.), it only render once while one-cell width character (a, ;, etc.) will be render twice.

In some case, Lighght cant not get the right width for characters, you can use a tuple (ch, width) to specify the width of character to avoid unexpected mess.

In double mode, a text character will still use one cell to render for one-cell width.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_size_double.gif" />
