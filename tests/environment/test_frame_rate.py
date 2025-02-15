import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.frame_rate(1)


@gh.draw
def draw():
    gh.background(' ')
    gh.text_size(gh.BIG)
    gh.text_align(gh.CENTER, gh.MIDDLE)
    gh.text(gh.get_frame_count(), gh.get_width() / 2, gh.get_height() / 2)


gh.run()
