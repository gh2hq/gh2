import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape()
gh.vertex(1, 1)
gh.vertex(6, 1)
gh.vertex(1, 6)
gh.end_shape()

gh.begin_shape()
gh.vertex(8, 1)
gh.vertex(13, 1)
gh.vertex(8, 6)
gh.end_shape(gh.CLOSE)

gh.run()