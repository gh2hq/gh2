import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.set_cursor(gh.get_width() / 2, gh.get_height() / 2)


@gh.draw
def draw():
    gh.background(' ')
    # check if cursor is moving, otherwise draw hint message
    if not gh.get_cursor_moved():
        gh.translate(gh.get_width() / 2, gh.get_height() / 2)
        gh.text_align(gh.CENTER)
        gh.stroke(' ', gh.WHITE, gh.BLACK)
        gh.text('Pressed up/right/down/left arrow.', 0, 0)


# You can use cursor_pressed hooks instead of
# mouse_moved or mouse_dragged to do some effects.

@gh.cursor_pressed
def cursor_pressed():
    x = gh.get_cursor_x()
    y = gh.get_cursor_y()
    px = gh.get_pcursor_x()
    py = gh.get_pcursor_y()

    gh.stroke('@', gh.YELLOW, gh.RED)
    gh.fill('+', gh.GREEN, gh.BLUE)
    gh.ellipse(x, y, 10, 10)

    gh.stroke('+', gh.CYAN, gh.MAGENTA)
    gh.point(px, py)


gh.run()
