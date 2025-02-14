import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# Outer shape
gh.begin_shape()

gh.vertex(0, 0)
gh.vertex(15, 0)
gh.vertex(15, 15)
gh.vertex(0, 15)

# Inner shape
gh.begin_contour()
gh.vertex(5, 5)
gh.vertex(5, 10)
gh.vertex(10, 10)
gh.vertex(10, 5)
gh.end_contour()

gh.end_shape(gh.CLOSE)

gh.run()