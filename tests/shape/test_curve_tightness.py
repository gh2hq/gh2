import gh2 as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('@', gh.YELLOW, gh.RED)
gh.fill('+', gh.GREEN, gh.BLUE)

# A curve with tightness of 1
with gh.open_context():
    gh.curve_tightness(1)
    gh.no_fill()
    gh.curve(-55, 26, 13, 24, 13, 11, -45, 25)

# A curve with tightness of 0
with gh.open_context():
    gh.translate(20, 0)
    gh.curve_tightness(0)  # default
    gh.no_fill()
    gh.curve(-55, 26, 13, 24, 13, 11, -45, 25)

gh.run()
