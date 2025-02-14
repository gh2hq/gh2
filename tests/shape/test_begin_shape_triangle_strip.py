import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.TRIANGLE_STRIP)
gh.vertex(1, 6)
gh.vertex(5, 1)
gh.vertex(10, 6)
gh.vertex(15, 1)
gh.vertex(20, 6)
gh.vertex(25, 1)
gh.vertex(30, 6)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()