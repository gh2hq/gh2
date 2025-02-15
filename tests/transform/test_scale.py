import gh2 as gh

gh.full_screen()
gh.no_cursor()

gh.stroke('%')
gh.rect(3, 2, 10, 6)
gh.scale(2, 2)
gh.rect(3, 2, 10, 6)

gh.run()