import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.CImage(100, 100)
img.load_pixels()
for i in range(img.width):
    for j in range(img.height):
        img.set(i, j, (255, 0, 0, 1))
img.update_pixels()
gh.image(img, 0, 0, 10, 5)

gh.run()
