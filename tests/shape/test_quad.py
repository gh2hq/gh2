import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.quad(
    9, 0,  # point1
    27 + 5, 2,  # point2
    19, 12,  # point3
    9, 7  # point4
)
gh.run()
