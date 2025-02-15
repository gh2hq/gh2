# Beating Heart

This is a beating heart made up of a rectangle and two circles full of 💘 to show double love.

![preview.md](https://raw.githubusercontent.com/charming-art/public-files/master/example_heart.gif)

```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen(gh.DOUBLE)
    gh.rect_mode(gh.RADIUS)
    gh.ellipse_mode(gh.RADIUS)
    gh.no_cursor()
    gh.frame_rate(10)


@gh.draw
def draw():
    size = 8
    x = gh.get_frame_count() / 2
    n1 = easing(x, size)
    n2 = easing(x + gh.PI, size)

    gh.background(" ")
    gh.no_stroke()
    gh.translate(gh.get_width() / 2, gh.get_height() / 2)
    gh.rotate(gh.QUARTER_PI)

    gh.fill('💘')
    gh.square(0, 0, size)
    gh.circle(0, -n1, size)
    gh.circle(n2, 0, size)


def easing(x, scale=1):
    p = gh.TAU * 2
    x = x - (x // p) * p
    if x < gh.PI:
        return gh.cos(x) * scale
    elif x < gh.PI * 2:
        return - scale
    elif x < gh.PI * 3:
        return gh.cos(x + gh.PI) * scale
    else:
        return scale

if __name__ == "__main__":
    gh.run()
```
