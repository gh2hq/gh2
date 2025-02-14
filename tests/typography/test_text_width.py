import lighght as gh

gh.full_screen()
gh.no_cursor()

text = 'charming'
width = gh.get_width()

th1 = gh.text_height(text)
gh.text(text, (width - gh.text_width(text)) / 2, 0)

gh.text_size(gh.BIG)
th2 = gh.text_height(text)
gh.text(text, (width - gh.text_width(text)) / 2, th1)

gh.text_size(gh.LARGE)
gh.text(text, (width - gh.text_width(text)) / 2, th1 + th2)

gh.run()
