import gh2 as gh

gh.full_screen()
gh.no_cursor()

img = gh.load_image('../assets/images/test.png')
img.load_pixels()
for i in range(int(img.width / 2)):
    for j in range(img.height):
        ri = img.width - i - 1
        color = img.get(i, j)
        img.set(ri, j, color)
img.update_pixels()

gh.image(img, 0, 0, 30, 15)
gh.run()
