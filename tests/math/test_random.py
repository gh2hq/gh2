import lighght as gh


bar_width = 5
bar_count = 0
bars = []


@gh.setup
def setup():
    global bars, bar_count
    gh.full_screen()
    gh.no_cursor()
    bar_count = gh.floor(gh.get_width() / bar_width)
    bars = [0 for _ in range(bar_count)]


@gh.draw
def draw():
    global bars
    i = int(gh.random(bar_count))
    bars[i] += 1

    gh.background(' ')
    gh.fill('Q')
    gh.no_stroke()

    for index, bar_height in enumerate(bars):
        gh.rect(
            bar_width * index,
            gh.get_height() - bar_height,
            bar_width,
            bar_height
        )


gh.run()
