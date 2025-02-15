import gh2 as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer  ellipse
gh.fill('O', gh.RED, gh.YELLOW)
gh.ellipse_mode(gh.RADIUS) 
gh.ellipse(12, 6, 12, 6)

# Inner ellipse
gh.fill('V', gh.BLUE, gh.GREEN)
gh.ellipse_mode(gh.CENTER)
gh.ellipse(12, 6, 12, 6)
gh.run()
