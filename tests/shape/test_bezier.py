import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.YELLOW, gh.RED)
gh.fill('+', gh.GREEN, gh.BLUE)

# only a bezier curve
with gh.open_context():
    gh.no_fill()
    gh.bezier(40, 5, 10, 10, 50, 20, 10, 30)

# a bezier curve with points
t = 0
cnt = 4
gh.translate(20, 0)
with gh.open_context():
    gh.no_fill()
    gh.bezier(40, 5, 10, 10, 50, 20, 10, 30)

    gh.stroke('a', gh.RED, gh.YELLOW)
    gh.stroke_weight(1)
    while t <= 1:
        x = gh.bezier_point(40, 10, 50, 10, t)
        y = gh.bezier_point(5, 10, 20, 30, t)
        gh.point(x, y)
        t += 1 / cnt

gh.run()
