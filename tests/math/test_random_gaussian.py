import gh2 as gh

gh.full_screen()
gh.no_cursor()

for y in range(gh.get_height()):
  mid = gh.get_width() / 2
  x = gh.random_gaussian(mid, 40)
  gh.stroke('$')
  gh.line(mid, y, x, y)

gh.run()