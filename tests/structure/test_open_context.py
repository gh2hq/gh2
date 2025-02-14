import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.ellipse(5, 5, 10, 5)

with gh.open_context():
  gh.fill('+', gh.YELLOW, gh.CYAN)
  gh.stroke('O', gh.BLUE, gh.GREEN)
  gh.translate(15, 0)
  gh.ellipse(5, 5, 10, 5)

gh.ellipse(35, 5, 10, 5)

gh.run()
