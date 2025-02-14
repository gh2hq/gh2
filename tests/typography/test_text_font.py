import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.text_size(gh.BIG)

font_list = gh.get_font_list()
text = 'charming'

th = gh.text_height(text)
gh.text(text, 0, 0)

gh.text_font(font_list[0])
th1 = gh.text_height(text)
gh.text(text, 0, th)

gh.text_font(font_list[1])
gh.text(text, 0, th + th1)

gh.run()
