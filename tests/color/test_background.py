# preview: https://raw.githubusercontent.com/charming-art/public-files/master/test_background.gif

import gh2 as gh


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
