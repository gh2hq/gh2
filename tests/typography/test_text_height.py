import lighght as gh

gh.full_screen()
gh.no_cursor()

text = 'C'
height = gh.get_height()
width = gh.get_width()

gh.text(text, 0, (height - gh.text_height(text)) / 2)

gh.text_size(gh.BIG)
gh.text(text, 10, (height - gh.text_height(text)) / 2)

gh.text_size(gh.LARGE)
gh.text(text, 20, (height - gh.text_height(text)) / 2)

gh.run()
