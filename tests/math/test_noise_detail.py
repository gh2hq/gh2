import lighght as gh


gh.full_screen()
gh.color_mode(gh.RGB)
gh.no_cursor()

gh.background(' ')
for j in range(gh.get_height()):
    for i in range(gh.get_width()):
        mid = gh.ceil(gh.get_width() / 2)
        dist = gh.abs(i - mid)
        noise_scale = 0.02
        if i < mid:
            gh.noise_detail(2, 0.2)
        else:
            gh.noise_detail(8, 0.65)
        v = gh.noise(dist * noise_scale, j * noise_scale)
        c = gh.map(v, 0, 1, 0, 255)
        gh.stroke(' ', (c,), (c,))
        gh.point(i, j)

gh.run()
