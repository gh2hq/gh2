# Typography

<a name="text" href="#text">#</a> gh.**text**(*text*, *x*, *y*)

Draws text to the screen. Displays the information specified in the first parameter on the screen in the position specified by the additional parameters.

A default font will be used unless a font is set with the text_font() function and a default size will be used unless a font is set with text_size(). Change the color of the text with the stroke() function. The text displays in relation to the text_align() function, which gives the option to draw to the left, right, and center of the coordinates.

```py
import gh2 as gh

# If you want to draw a ascii text, you'd
# better use raw string: r'''xxx'''.
head = r'''
         .-"""-.
        /       \
        \       /
 .-"""-.-`.-.-.<  _
/      _,-\ ()()_/:)
\     / ,  `     `|
 '-..-| \-.,___,  /
       \ `-.__/  /
        `-.__.-'`
'''

face = "(^O^)/"

gh.full_screen()
gh.no_cursor()

gh.stroke(fg=gh.RED, bg=gh.YELLOW)
gh.text(head, 0, 0)
gh.text(face, 25, 5)

gh.stroke_weight(1)
gh.text('h', 35, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text.png" />

<a name="text_width" href="#text_width">#</a> gh.**text_width**(*text*) : *number*

Calculates and returns the width of any character or text string.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

text = 'charming'
width = gh.get_width()

th1 = gh.text_height(text)
gh.text(text, (width - gh.text_width(text)) / 2, 0)

gh.text_size(gh.BIG)
th2 = gh.text_height(text)
gh.text(text, (width - gh.text_width(text)) / 2, th1)

gh.text_size(gh.LARGE)
gh.text(text, (width - gh.text_width(text)) / 2, th1 + th2)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_width.png" />

<a name="text_align" href="#text_align">#</a> gh.**text_align**(*align_x*=LEFT | RIGHT | CENTER[, *align_y*=TOP | BOTTOM | MIDDLE])

Sets the current alignment for drawing text.The parameters LEFT, CENTER, and RIGHT set the display characteristics of the letters in relation to the values for the x and y parameters of the text() function.

```py
import gh2 as gh

text = 'charming'

gh.full_screen()
gh.no_cursor()
gh.translate(gh.get_width() / 2, gh.get_height() / 2)

gh.stroke('|')
gh.line(0, -gh.get_height() / 2, 0, gh.get_height() / 2)

# left
gh.text_align(gh.LEFT)
gh.text(text, 0, -5)

# center
gh.text_align(gh.CENTER)
gh.text(text, 0, 0)

# right
gh.text_align(gh.RIGHT)
gh.text(text, 0, 5)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_align_x.png" />

```py
import gh2 as gh

text = 'ch'

gh.full_screen()
gh.no_cursor()
gh.translate(gh.get_width() / 2, gh.get_height() / 2)

gh.stroke('-')
gh.line(-gh.get_width() / 2, 0, gh.get_width() / 2, 0)
gh.text_size(gh.BIG)

# top
gh.text_align(gh.CENTER, align_y=gh.TOP)
gh.text(text, -20, 0)

# middle
gh.text_align(align_y=gh.MIDDLE)
gh.text(text, 0, 0)

# bottom
gh.text_align(align_y=gh.BOTTOM)
gh.text(text, 20, 0)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_align_y.png" />

<a name="text_size" href="#text_size">#</a> gh.**text_size**(*size*=NORMAL | BIG |LARGE))

Sets the current font size.

```py
import gh2 as gh

text = 'charming'

gh.full_screen()
gh.no_cursor()

gh.text(text, 0, 0)

gh.text_size(gh.BIG)
gh.text(text, 0, 2)

gh.text_size(gh.LARGE)
gh.text(text, 0, 8)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_size.png" />

<a name="text_height" href="#text_height">#</a> gh.**text_height**(*text*) : *number*

Calculates and returns the height of any character or text string.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

text = 'C'
height = gh.get_height()
width = gh.get_width()

gh.text(text, 0, (height - gh.text_height(text)) / 2)

gh.text_size(gh.BIG)
gh.text(text, 10, (height - gh.text_height(text)) / 2)

gh.text_size(gh.LARGE)
gh.text(text, 20, (height - gh.text_height(text)) / 2)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_height.png" />

<a name="get_font_list" href="#get_font_list">#</a> gh.**get_font_list**(*text*, *x*, *y*) : *string[]*

Returns the supported font list for text with BIG font size.

```py
import gh2 as gh

font_list = gh.get_font_list()

print(font_list) # ['clb6x10', 'nipples', 'computer', ...]
print(len(font_list)) # 425
```

<a name="text_font" href="#text_font">#</a> gh.**text_font**(*name*)

Sets the current font that will be drawn with the text() function.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()
gh.text_size(gh.BIG)

font_list = gh.get_font_list()
text = 'charming'

th = gh.text_height(text)
gh.text(text, 0, 0)

gh.text_font(font_list[0])
th1 = gh.text_height(text)
gh.text(text, 0, th)

gh.text_font(font_list[1])
gh.text(text, 0, th + th1)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_font.png" />