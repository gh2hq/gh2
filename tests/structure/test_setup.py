import lighght as gh


a = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.background('O')
    gh.fill('+', gh.YELLOW, gh.CYAN)
    gh.no_stroke()


@gh.draw
def draw():
    global a
    gh.rect(a % gh.get_width(), 2, 2, gh.get_height() - 4)
    a += 1


gh.run()
