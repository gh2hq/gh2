import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer  rect
gh.fill('O', gh.RED, gh.YELLOW)
gh.rect_mode(gh.RADIUS) 
gh.rect(12, 6, 10, 5)

# Inner rect
gh.fill('V', gh.BLUE, gh.GREEN)
gh.rect_mode(gh.CENTER)
gh.rect(12, 6, 10, 5)
gh.run()