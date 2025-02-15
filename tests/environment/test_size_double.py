import gh2 as gh

chars = ['💘', '🌈', 'A', ('⏰', 2), '🧚', '爱']
texts = [
    'hello world',
    '🚀🚀h',
    'h🚀llo'
]

x = 0


@gh.setup
def setup():
    gh.size(30, 20, gh.DOUBLE)
    gh.frame_rate(2)
    gh.no_cursor()


@gh.draw
def draw():
    global x
    size = 5
    ch = chars[gh.get_frame_count() % len(chars)]
    y = 10
    x += 2

    gh.background(" ")
    gh.no_stroke()
    gh.fill(ch)

    # polygan
    gh.begin_shape()
    gh.vertex(x, y)
    gh.vertex(x + size, y)
    gh.vertex(x + size, y - size)
    gh.vertex(x + size * 2, y)
    gh.vertex(x, y + size * 2)
    gh.end_shape(gh.CLOSE)

    # text
    gh.stroke()
    for i, t in enumerate(texts):
        gh.text(t, 0, i)


gh.run()
