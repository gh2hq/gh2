import gh2 as gh

gh.full_screen()
gh.no_cursor()

for i in range(256):
    x = i % 32
    y = i // 32
    gh.stroke(' ', i, i)
    gh.point(x, y)

gh.run()
