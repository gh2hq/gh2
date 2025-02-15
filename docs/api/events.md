# Events

Methods for listening and handling events.

## Keyboard

Methods for keyboard events.

<a name="get_key" href="#get_key">#</a> gh.**get_key**() : *string*

The system variable key always contains the value of the most recent key on the keyboard that was used (either pressed or released).

<a name="get_key_pressed" href="#get_key_pressed">#</a> gh.**get_key_code**() : *boolean*

The boolean system variable key_pressed is true if any key is pressed and false if no keys are pressed.

```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    if gh.get_key_pressed():
        key = gh.get_key()
        if key == 'b' or key == 'B':
            gh.fill('O')
        else:
            gh.fill('+')
    gh.no_stroke()
    gh.rect(0, 0, 10, 10)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key.gif" width="100%"/>

<a name="get_key_code" href="#get_key_code">#</a> gh.**get_key_code**() : *number*

The variable keyCode is used to detect special keys such as the arrow keys (UP, DOWN, LEFT, and RIGHT) as well as ENTER, SPACE.

<a name="key_pressed" href="#key_pressed">#</a> gh.**key_pressed**(*foo*)

The function decorated by key_pressed decorator is called once every time a key is pressed.

```py
import gh2 as gh

# CODED, ESCAPE, LEFT, UP, RIGHT, DOWN, BACKSPACE, TAB, ENTER, SPACE

char = ''


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.no_stroke()
    gh.rect(0, 0, 10, 10)


@gh.key_pressed
def key_pressed():
    global char
    if gh.get_key() == gh.CODED:
        if gh.get_key_code() == gh.UP:
            char = 'O'
        else:
            char = '+'


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key_code.gif" width="100%"/>

<a name="key_released" href="#key_released">#</a> gh.**key_released**(*foo*)

The function decorated by key_released decorator is called once every time a key is released.

```py
import gh2 as gh

char = ''


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.no_stroke()
    gh.rect(0, 0, 10, 10)


@gh.key_released
def key_released():
    global char
    if gh.get_key() == gh.CODED:
        if gh.get_key_code() == gh.UP:
            char = 'O'
        else:
            char = '+'


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key_code.gif" width="100%"/>

<a name="key_typed" href="#key_typed">#</a> gh.**key_typed**(*foo*)

The function decorated by key_typed decorator is called once every time a key is typed.

```py
import gh2 as gh

char = ''


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.no_stroke()
    gh.rect(0, 0, 10, 10)


@gh.key_typed
def key_typed():
    global char
    if gh.get_key() == gh.CODED:
        if gh.get_key_code() == gh.UP:
            char = 'O'
        else:
            char = '+'


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key_code.gif" width="100%"/>

## Mouse

Methods for mouse events.

<a name="get_mouse_x" href="#get_mouse_x">#</a> gh.**get_mouseX**() : *number*

The system variable mouse_x always contains the current horizontal coordinate of the mouse.

<a name="get_mouse_y" href="#get_mouse_y">#</a> gh.**get_mouseY**() : *number*

The system variable mouse_y always contains the current vertical coordinate of the mouse.

```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    mouse_x = gh.get_mouse_x()
    mouse_y = gh.get_mouse_y()
    gh.line(mouse_x, 0, mouse_x, gh.get_height())
    gh.line(0, mouse_y, gh.get_width(), mouse_y)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_pos.gif" width="100%"/>

<a name="get_mouse_pressed" href="#get_mouse_pressed">#</a> gh.**get_mouse_pressed**() : *boolean*

The mouse_pressed variable stores whether or not a mouse button is currently being pressed.

<a name="get_mouse_button" href="#get_mouse_button">#</a> gh.**get_mouse_button**() : *boolean*

When a mouse button is pressed, the value of the system variable mouseButton is set to either LEFT, RIGHT, or CENTER, depending on which button is pressed.

```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()


@gh.draw
def draw():
    gh.no_stroke()
    if gh.get_mouse_pressed() and gh.get_mouse_button() == gh.LEFT:
        gh.fill('O')
    elif (gh.get_mouse_pressed() and gh.get_mouse_button() == gh.RIGHT):
        gh.fill('+')
    else:
        gh.fill('-')
    gh.rect(0, 0, 10, 10)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

<a name="mouse_clicked" href="#mouse_clicked">#</a> gh.**mouse_clicked**(*foo*)

```py
import gh2 as gh

char = 'O'


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.rect(0, 0, 10, 10)


@gh.mouse_clicked
def mouse_clicked():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

<a name="mouse_pressed" href="#mouse_pressed">#</a> gh.**mouse_pressed**(*foo*)

The function decorated mouse_released decorator is called after a mouse button has been pressed.

```py
import gh2 as gh

char = 'O'


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.rect(0, 0, 10, 10)


@gh.mouse_pressed
def mouse_pressed():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

<a name="mouse_released" href="#mouse_released">#</a> gh.**mouse_released**(*foo*)

```py
import gh2 as gh

char = 'O'


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.rect(0, 0, 10, 10)


@gh.mouse_released
def mouse_released():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

## Cursor

Methods for cursor events.

<a name="get_cursor_x" href="#get_cursor_x">#</a> gh.**get_cursor_x**() : *number*

The system variable cursor_x always contains the current horizontal coordinate of the cursor.

<a name="get_cursor_y" href="#get_cursor_y">#</a> gh.**get_cursor_y**() : *number*

The system variable cursor_y always contains the current vertical coordinate of the cursor.

<a name="get_pcursor_x" href="#get_pcursor_x">#</a> gh.**get_pcursor_x**() : *number*

The system variable pcursor_x always contains the horizontal position of the cursor in the frame previous to the current frame.

<a name="get_pcursor_y" href="#get_pcursor_y">#</a> gh.**get_pcursor_y**() : *number*

The system variable pcursor_y always contains the vertical position of the cursor in the frame previous to the current frame.

<a name="cursor_moved" href="#cursor_moved">#</a> gh.**cursor_moved**(*foo*)

The function decorated cursor_moved decorator is called after a cursor moved.

<a name="cursor_pressed" href="#cursor_pressed">#</a> gh.**cursor_pressed**(*foo*)

The function decorated cursor_pressed decorator is called after a cursor pressed.

<a name="get_cursor_moved" href="#get_cursor_moved">#</a> gh.**get_cursor_moved**() : *number*

The boolean system variable cursor_moved is true if any cursor is pressed and false if cursor is not pressed.

```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.set_cursor(gh.get_width() / 2, gh.get_height() / 2)


@gh.draw
def draw():
    gh.background(' ')
    # check if cursor is moving, otherwise draw hint message
    if not gh.get_cursor_moved():
        gh.translate(gh.get_width() / 2, gh.get_height() / 2)
        gh.text_align(gh.CENTER)
        gh.stroke(' ', gh.WHITE, gh.BLACK)
        gh.text('Pressed up/right/down/left arrow.', 0, 0)


# You can use cursor_pressed hooks instead of
# mouse_moved or mouse_dragged to do some effects.

@gh.cursor_pressed
def cursor_pressed():
    x = gh.get_cursor_x()
    y = gh.get_cursor_y()
    px = gh.get_pcursor_x()
    py = gh.get_pcursor_y()

    gh.stroke('@', gh.YELLOW, gh.RED)
    gh.fill('+', gh.GREEN, gh.BLUE)
    gh.ellipse(x, y, 10, 10)

    gh.stroke('+', gh.CYAN, gh.MAGENTA)
    gh.point(px, py)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_event_cursor.gif" width="100%"/>