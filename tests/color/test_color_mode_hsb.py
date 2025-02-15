import gh2 as gh

gh.full_screen()
gh.color_mode(gh.HSB)
gh.no_cursor()

# rainbows
w = 30
h = 360 / w

for hue in range(360):
    i = hue % w
    j = hue // w
    gh.stroke(" ", (hue, 100, 100), (hue, 100, 100))
    gh.point(i, j)

gh.run()