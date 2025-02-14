import lighght as gh

text = 'charming'

gh.full_screen()
gh.no_cursor()
gh.translate(gh.get_width() / 2, gh.get_height() / 2)

gh.stroke('|')
gh.line(0, -gh.get_height() / 2, 0, gh.get_height() / 2)

# left
gh.text_align(gh.LEFT)
gh.text(text, 0, -5)

# center
gh.text_align(gh.CENTER)
gh.text(text, 0, 0)

# right
gh.text_align(gh.RIGHT)
gh.text(text, 0, 5)


gh.run()
