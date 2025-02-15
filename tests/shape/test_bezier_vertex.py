import gh2 as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom curve
with gh.open_shape():
    gh.vertex(30, 5)
    gh.bezier_vertex(80, 0, 80, 35, 30, 35)
    gh.bezier_vertex(50, 30, 60, 25, 30, 5)

gh.run()