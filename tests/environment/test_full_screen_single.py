import gh2 as gh

x = 0


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    global x
    gh.background(' ')
    gh.rect(x, 0, 10, 10)
    x += 1


gh.run()
