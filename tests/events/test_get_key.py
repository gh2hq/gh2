import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    if gh.get_key_pressed():
        key = gh.get_key()
        if key == 'b' or key == 'B':
            gh.fill('O')
        else:
            gh.fill('+')
    gh.no_stroke()
    gh.rect(0, 0, 10, 10)


gh.run()
