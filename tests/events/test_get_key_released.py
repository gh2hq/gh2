import gh2 as gh

char = ''


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.no_stroke()
    gh.rect(0, 0, 10, 10)


@gh.key_released
def key_released():
    global char
    if gh.get_key() == gh.CODED:
        if gh.get_key_code() == gh.UP:
            char = 'O'
        else:
            char = '+'


gh.run()
