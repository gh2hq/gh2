import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

with gh.open_shape(gh.LINES, gh.CLOSE):
    gh.vertex(1, 1)
    gh.vertex(6, 1)
    gh.vertex(6, 6)
    gh.vertex(1, 6)

gh.run()
