import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer  ellipse
gh.fill('O', gh.RED, gh.YELLOW)
gh.ellipse_mode(gh.CORNER) 
gh.ellipse(8, 4, 16, 8)

# Inner ellipse
gh.fill('V', gh.BLUE, gh.GREEN)
gh.ellipse_mode(gh.CORNERS)
gh.ellipse(8, 4, 16, 8)
gh.run()
