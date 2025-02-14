import lighght as gh

frames = None


@gh.setup
def setup():
    global frames
    gh.full_screen()
    gh.no_cursor()
    frames = gh.load_image('../assets/images/test.gif')


@gh.draw
def draw():
    gh.background(' ')
    index = int(gh.get_frame_count() / 2) % len(frames)
    frame = frames[index]
    gh.image(frame, 0, 0, 30, 15)


gh.run()
