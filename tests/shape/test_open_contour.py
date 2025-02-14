import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# Shapes
gh.begin_shape()
with gh.open_shape(close_mode=gh.CLOSE):
  gh.vertex(0, 0)
  gh.vertex(15, 0)
  gh.vertex(15, 15)
  gh.vertex(0, 15)
  with gh.open_contour():
    gh.vertex(5, 5)
    gh.vertex(5, 10)
    gh.vertex(10, 10)
    gh.vertex(10, 5)

gh.run()