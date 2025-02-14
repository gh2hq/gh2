import lighght as gh

gh.full_screen()
gh.no_cursor()

gh.fill('@', gh.RED, gh.BLUE)
gh.rect(0, 0, 10, 5)

gh.fill('O', gh.YELLOW, gh.CYAN)
gh.rect(20, 0, 10, 5)

gh.run()