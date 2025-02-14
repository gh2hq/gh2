import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.stroke_weight(0) # Default
gh.stroke('O')
gh.line(3, 0, 25, 0)

gh.stroke('A')
gh.stroke_weight(1) # Thicker
gh.line(3, 3, 25, 3)

gh.stroke('X')
gh.stroke_weight(2) # Beastly
gh.line(3, 8, 25, 8)

gh.run()