import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.YELLOW, gh.RED)
gh.fill('+', gh.GREEN, gh.BLUE)

# A curve with some points
with gh.open_context():
    gh.no_fill()
    gh.curve(-55, 26, 13, 24, 13, 11, -45, 25)

    t = 0
    cnt = 3
    gh.stroke('p', gh.CYAN, gh.RED)
    gh.stroke_weight(1)
    while t <= 1:
        x = gh.curve_point(-55, 13, 13, -45, t)
        y = gh.curve_point(26, 24, 11, 25, t)
        gh.point(x, y)
        t += 1 / cnt


gh.run()
