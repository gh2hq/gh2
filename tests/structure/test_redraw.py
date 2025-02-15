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
