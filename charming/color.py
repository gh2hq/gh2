from . import constants
from .core import Color
from .app import renderer
from .common import check_color
from .utils import lerp_color as utils_lerp_color
from .utils import logger
from .utils import map


@check_color
def stroke(ch=" ", fg=None, bg=None):
    renderer.is_stroke_enabled = True
    c = Color(ch, fg, bg)
    renderer.stroke_color = c


@check_color
def fill(ch=" ", fg=None, bg=None):
    renderer.is_fill_enabled = True
    if ch == " ":
        c = Color.empty()
    else:
        c = Color(ch, fg, bg)
    renderer.fill_color = c


def no_stroke():
    renderer.is_stroke_enabled = False


def no_fill():
    renderer.is_fill_enabled = False


@check_color
def background(ch=" ", fg=None, bg=None):
    if ch == " ":
        c = Color.empty()
    else:
        c = Color(ch, fg, bg)
    renderer.background(c)


def lerp_color(start, stop, amt):
    if Color.color_mode == constants.ANSI:
        start = map(start, 0, Color.color_channels[0], 0, 255)
        stop = map(stop, 0, Color.color_channels[0], 0, 255)

        start = Color.ansi256_to_rgb(round(start))
        stop = Color.ansi256_to_rgb(round(stop))

        r, g, b = utils_lerp_color([start, stop], amt)

        v = Color.rgb_to_ansi256(r, g, b)
        v = map(v, 0, 255, 0, Color.color_channels[0])
        return v
    else:
        start = (
            start[0] / Color.color_channels[0],
            start[1] / Color.color_channels[1],
            start[2] / Color.color_channels[2],
        )
        stop = (
            stop[0] / Color.color_channels[0],
            stop[1] / Color.color_channels[1],
            stop[2] / Color.color_channels[2],
        )

        if Color.color_mode == constants.HSB:
            start = Color.hsb_to_rgb(start[0], start[1], start[2])
            stop = Color.hsb_to_rgb(stop[0], stop[1], stop[2])

        v1, v2, v3 = utils_lerp_color([start, stop], amt)

        if Color.color_mode == constants.HSB:
            v1, v2, v3 = Color.rgb_to_hsb(v1, v2, v3)

        v1, v2, v3 = [
            map(v, 0, 1, 0, Color.color_channels[i])
            for i, v in enumerate([v1, v2, v3])
        ]
        return (v1, v2, v3)


def color_mode(mode=constants.ANSI, max1=None, max2=None, max3=None):
    Color.color_mode = mode
    if mode == constants.ANSI:
        if max1 != None:
            Color.color_channels = (max1,)
    else:
        if max1 != None and (max2 == None and max3 == None):
            Color.color_channels = (max1, max1, max1)
        elif max1 != None and max2 != None and max3 != None:
            Color.color_channels = (max1, max2, max3)
        else:
            if mode == constants.RGB:
                Color.color_channels = (255, 255, 255)
            else:
                Color.color_channels = (360, 100, 100)
