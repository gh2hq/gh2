import lighght as gh


@gh.setup
def setup():
    gh.full_screen()


@gh.draw
def draw():
    gh.no_stroke()
    if gh.get_mouse_pressed() and gh.get_mouse_button() == gh.LEFT:
        gh.fill('O')
    elif (gh.get_mouse_pressed() and gh.get_mouse_button() == gh.RIGHT):
        gh.fill('+')
    else:
        gh.fill('-')
    gh.rect(0, 0, 10, 10)


gh.run()
