import gh2 as gh

char = 'O'


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    gh.fill(char)
    gh.rect(0, 0, 10, 10)


@gh.mouse_pressed
def mouse_pressed():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


gh.run()
