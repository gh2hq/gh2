import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.color_mode(gh.RGB)

gh.random_seed(99)
for i in range(gh.get_width()):
    r = gh.random(0, 255)
    gh.stroke(' ', (r,), (r, ))
    gh.line(i, 0, i, gh.get_height())

gh.run()
