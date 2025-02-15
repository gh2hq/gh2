import gh2 as gh

gh.full_screen()
gh.color_mode(gh.RGB)
gh.no_cursor()

n = 7
gh.stroke_weight(1)

for i in range(n):
    c = gh.map(i, 0, n, 0, 255)
    gh.stroke("@", (c,), (c,))
    gh.point(i * 5 + 5, 2)

gh.run()
