import lighght as gh

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
