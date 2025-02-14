import lighght as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    mouse_x = gh.get_mouse_x()
    mouse_y = gh.get_mouse_y()
    gh.line(mouse_x, 0, mouse_x, gh.get_height())
    gh.line(0, mouse_y, gh.get_width(), mouse_y)


gh.run()
