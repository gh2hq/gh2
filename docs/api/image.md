# Image

Methods for drawing image to screen.

## CImage

Date type for gh2 to store and manipulate image.

<a name="cimage" href="#cimage">#</a> gh.**CImage**(*data*, *width*, *height*) : CImage

Creates a new CImage (the datatype for storing images). This provides a fresh buffer of pixels to play with. Set the size of the buffer with the width and height parameters.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.CImage(100, 100)
img.load_pixels()
for i in range(img.width):
    for j in range(img.height):
        img.set(i, j, (255, 0, 0, 1))
img.update_pixels()
gh.image(img, 0, 0, 10, 5)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_cimage.png" />

<a name="load_pixels" href="#load_pixels">#</a> CImage.**load_pixels**()

Loads the pixels data for this image into the `pixels` attribute.

<a name="update_pixels" href="#update_pixels">#</a> CImage.**update_pixels**()

Updates the backing canvas for this image with the contents of the `pixels` array.

<a name="set" href="#set">#</a> CImage.**set**(*x*, *y*, *color*)

Set the color of a single pixel.

<a name="get" href="#get">#</a> CImage.**get**(*x*, *y*) : (r, g, b, a)

Get the color of a single pixel.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
img.load_pixels()
for i in range(int(img.width / 2)):
    for j in range(img.height):
        ri = img.width - i - 1
        color = img.get(i, j)
        img.set(ri, j, color)
img.update_pixels()

gh.image(img, 0, 0, 30, 15)
gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_cimage_method.png" />

## Display

Methods for display images.

<a name="image" href="#image">#</a> gh.**image**(*image*, *a*, *b*, *c*, *d*)

Draw an image to the p5.js canvas which will be affected by **cm**.*rect_mode*.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
gh.image(img, 0, 0, 30, 15)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_image.png" />

<a name="load_image" href="#load_image">#</a> gh.**load_image**(*src*) : CImage

Loads an image from a path and creates a CImage or CImage array from it.

If it loads a static image such as png format, it will returns a CImage.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
gh.image(img, 0, 0, 30, 15)

gh.run()
```

If it loads a active image such as gif format, it will returns a CImage array.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_image.png" />

```py
import gh2 as gh

frames = None


@gh.setup
def setup():
    global frames
    gh.full_screen()
    gh.no_cursor()
    frames = gh.load_image('../assets/images/test.gif')


@gh.draw
def draw():
    gh.background(' ')
    index = int(gh.get_frame_count() / 2) % len(frames)
    frame = frames[index]
    gh.image(frame, 0, 0, 30, 15)


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_load_image.gif" />

<a name="no_tint" href="#no_tint">#</a> gh.**no_tint**()

Removes the current fill value for displaying images and reverts to displaying images with their original color.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
gh.tint('O', gh.RED)
gh.image(img, 0, 0, 30, 15)

gh.no_tint()
gh.image(img, 32, 0, 30, 15)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_tint.png" />

<a name="tint" href="#tint">#</a> gh.**tint**(*ch*=" "[, *fg*[, *bg*]])<br>
<a name="tint" href="#tint">#</a> gh.**tint**(*ccolor*)

Sets the fill value for displaying images. Images can be tinted to specified character and foreground color.

```py
import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
gh.tint('O', gh.RED)
gh.image(img, 0, 0, 30, 15)

gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_tint.png" />
