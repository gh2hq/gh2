import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('%')
gh.translate(gh.get_width() / 2, gh.get_height() / 2)
gh.shear_y(gh.PI / 3.0)
gh.rect(-5, -5, 10, 10)


gh.run()
