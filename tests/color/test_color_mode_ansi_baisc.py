import gh2 as gh

gh.full_screen()
gh.no_cursor()

# basic colors
colors = [
    gh.RED,
    gh.BLACK,
    gh.CYAN,
    gh.YELLOW,
    gh.GREEN,
    gh.BLUE,
    gh.WHITE,
    gh.MAGENTA
]

gh.stroke_weight(1)
for i, c in enumerate(colors):
    x = 5
    y = 2
    gh.stroke("@", c, c)
    gh.point(i * 5 + x , y)

gh.run()
