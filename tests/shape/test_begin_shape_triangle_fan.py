import gh2 as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.TRIANGLE_FAN)
gh.vertex(11, 6)
gh.vertex(11, 1)
gh.vertex(21, 6)
gh.vertex(11, 11)
gh.vertex(1, 6)
gh.vertex(11, 1)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()