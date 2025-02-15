import gh2 as gh

text = 'ch'

gh.full_screen()
gh.no_cursor()
gh.translate(gh.get_width() / 2, gh.get_height() / 2)

gh.stroke('-')
gh.line(-gh.get_width() / 2, 0, gh.get_width() / 2, 0)
gh.text_size(gh.BIG)

# top
gh.text_align(gh.CENTER, align_y=gh.TOP)
gh.text(text, -20, 0)

# middle
gh.text_align(align_y=gh.MIDDLE)
gh.text(text, 0, 0)

# bottom
gh.text_align(align_y=gh.BOTTOM)
gh.text(text, 20, 0)


gh.run()
