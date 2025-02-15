import gh2 as gh

text = 'charming'

gh.full_screen()
gh.no_cursor()

gh.text(text, 0, 0)

gh.text_size(gh.BIG)
gh.text(text, 0, 2)

gh.text_size(gh.LARGE)
gh.text(text, 0, 8)

gh.run()