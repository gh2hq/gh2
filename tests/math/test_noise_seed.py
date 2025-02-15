import gh2 as gh


xoff = 0.0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.noise_seed(99)


@gh.draw
def draw():
    gh.background(' ')
    global xoff
    xoff += .01
    n = gh.noise(xoff) * gh.get_width()
    gh.line(n, 0, n, gh.get_height())


gh.run()
