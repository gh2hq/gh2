import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom curve
with gh.open_shape():
    gh.curve_vertex(44, 21)
    gh.curve_vertex(44, 21)
    gh.curve_vertex(48, 9)
    gh.curve_vertex(21, 7)
    gh.curve_vertex(2, 30)
    gh.curve_vertex(2, 30)

gh.run()
