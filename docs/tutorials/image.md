# Image

In gh2, it is possible for you to draw an image to terminal as simple as Processing, but only a subset of raw pixels will be displayed.

## Static image

```py
''' gh2: image '''

import gh2 as app

app.no_cursor()
app.full_screen()
img = app.load_image('avatar.png')
app.image(img, 0, 0, 60, 30)

app.run()
```

![image](https://raw.githubusercontent.com/charming-art/public-files/master/image.png)

<!-- ## Image Animation -->
