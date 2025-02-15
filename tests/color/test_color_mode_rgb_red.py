import gh2 as gh

gh.full_screen()
gh.no_cursor()
gh.color_mode(gh.RGB)

n = 7
gh.stroke_weight(1)

for i in range(n):
    c = gh.map(i, 0, n, 0, 255)
    gh.stroke(" ", (c, 0, 0), (c, 0, 0))
    gh.point(i * 5 + 5, 2)

gh.run()
