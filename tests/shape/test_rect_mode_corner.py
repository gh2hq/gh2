import lighght as gh

gh.full_screen()
gh.no_cursor()
gh.no_stroke()

# Outer rect
gh.fill('O', gh.RED, gh.YELLOW)
gh.rect_mode(gh.CORNER) 
gh.rect(8, 4, 16, 8)

# Inner rect
gh.fill('V', gh.BLUE, gh.GREEN)
gh.rect_mode(gh.CORNERS)
gh.rect(8, 4, 16, 8)
gh.run()