import gh2 as gh

gh.full_screen()
gh.no_cursor()
gh.color_mode(gh.RGB)

start = gh.CColor('a', (0,), (255, 0, 0))
end = gh.CColor('z', (255, 255, 0), (0,))
n = 10

for i in range(n):
    t = i / n
    c = gh.lerp_color(start, end, t)
    gh.stroke_weight(1)
    gh.stroke(c)
    gh.point(i * 5 + 5, 2)

gh.run()