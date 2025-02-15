import gh2 as gh

gh.full_screen()
gh.no_cursor()

start = gh.CColor('a', gh.BLUE, gh.RED)  # start color
end = gh.CColor('z', gh.GREEN, gh.YELLOW)  # end color

gh.stroke_weight(1)
n = 10
for i in range(n):
    t = i / n
    c = gh.lerp_color(start, end, t)
    gh.stroke(c)
    gh.point(i * 5 + 5, 2)

gh.run()
