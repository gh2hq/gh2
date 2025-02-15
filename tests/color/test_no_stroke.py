import gh2 as gh

gh.full_screen()
gh.no_cursor()

gh.fill('@', gh.RED, gh.BLUE)
gh.rect(0, 0, 10, 5)

gh.no_stroke()
gh.rect(20, 0, 10, 5)

gh.run()