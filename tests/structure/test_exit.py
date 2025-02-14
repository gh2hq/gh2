import lighght as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.color_mode(gh.RGB)


@gh.draw
def draw():
    b = gh.get_frame_count() % 255
    color = (0, 0, b)
    gh.background(' ', color, color)


@gh.mouse_clicked
def mouse_clicked():
    gh.exit()


gh.run()
