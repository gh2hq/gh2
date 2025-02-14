import lighght as gh


xoff = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    global xoff
    gh.background(' ')
    xoff += 0.01
    n = gh.noise(xoff) * gh.get_width()
    gh.line(n, 0, n, gh.get_height())


gh.run()
