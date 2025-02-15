import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
gh.tint('O', gh.RED)
gh.image(img, 0, 0, 30, 15)

gh.no_tint()
gh.image(img, 32, 0, 30, 15)

gh.run()