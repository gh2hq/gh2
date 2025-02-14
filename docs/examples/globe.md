# Cherry Blossom Globe

A cherry blossom gif and a globe gif can create a wonderful world by Lighght. [[source](../../examples/globe.py)]

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_globe_globe.gif" height="200px"/> &emsp; <img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_globe_fall.gif" height="200px" />

![preview.md](https://raw.githubusercontent.com/charming-art/public-files/master/example_globe.gif)

```py
import lighght as gh

globe_frames = None
fall_frames = None


@gh.setup
def setup():
    global globe_frames, fall_frames
    gh.full_screen(gh.DOUBLE)
    gh.frame_rate(5)
    gh.no_cursor()
    fall_frames = gh.load_image("images/fall.gif")
    globe_frames = gh.load_image("images/globe.gif")


@gh.draw
def draw():
    gh.background()
    width = gh.get_width()
    height = gh.get_height()
    w = 30
    h = 30
    x = (width - w) / 2
    y = (height - h) / 2
    fall_img = fall_frames[gh.get_frame_count() % len(fall_frames)]
    globe_img = globe_frames[gh.get_frame_count() % len(globe_frames)]

    gh.image(globe_img, x, y, w, h)
    gh.image(fall_img, 0, 0, width, height)


if __name__ == "__main__":
    gh.run()

```
