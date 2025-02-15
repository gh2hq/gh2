import gh2 as gh

gh.full_screen()
gh.no_cursor()

x = gh.get_width() / 2
y = gh.get_height() / 2
r = gh.get_height() * 0.8

gh.arc(x, y, r * 2, r, 0, gh.TWO_PI, gh.PIE)

gh.run()