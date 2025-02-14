# Covid-19 Bar Chart

There is a bar chart for mock data about covid-19 virus created by Lighght. Instead of only using green for the curve, red for the confirm, gray for the dead, it also use 🌈 to express happiness and hope, use 🦠 to strengthen the warning, and use ☠️ to show sadness and fear. They are indeed make this chart more vivid and unforgettable. [[source](../../examples/bar.py)]

![preview.md](https://raw.githubusercontent.com/charming-art/public-files/master/example_barchart.png)

```py
import lighght as gh
from scales import scale_linear, scale_band, scale_ordinal

# mock data
data = [
    {
        'name': 'curve',
        'value': 10,
    },
    {
        'name': 'confirm',
        'value': 30,
    },
    {
        'name': 'suspect',
        'value': 15,
    },
    {
        'name': 'dead',
        'value': 5,
    },
]

# open canvas
gh.full_screen(gh.DOUBLE)
gh.no_cursor()

# chart options
margin = {
    'top': 5,
    'right': 5,
    'bottom': 5,
    'left': 5
}
width = gh.get_width() - margin['left'] - margin['right']
height = gh.get_height() - margin['top'] - margin['bottom']

# scales
max_data = gh.max(data, key=lambda d: d['value'])
names = [d['name'] for d in data]
colors = [
    ('🌈', gh.GREEN),
    ('🦠', gh.RED),
    (('⚠️', 2), gh.YELLOW),
    (('☠️', 2), gh.WHITE)
]
x_scale = scale_band(names, [0, width], padding=2)
y_scale = scale_linear([0, max_data['value']], [height, 0])
color_scale = scale_ordinal(names, colors)

# draw
gh.translate(margin['left'], margin['top'])

# bars
for d in data:
    name, value = d['name'], d['value']
    x = x_scale(name)
    y = y_scale(value)
    bw = x_scale.band_width()
    ch, bg = color_scale(name)

    # bars
    gh.no_stroke()
    gh.fill(ch, bg=bg)
    gh.rect(x, y, int(bw), height - y)

    # value
    gh.stroke()
    gh.text_align(gh.CENTER)
    gh.text(str(value), x + bw / 2 + 1, y - 2)

# bottom axes
gh.stroke('-')
gh.line(0, height, width, height)
for name in x_scale.domain():
    x = x_scale(name)
    bw = x_scale.band_width()
    gh.stroke()
    gh.text_align(gh.CENTER)
    gh.text(name, x + bw / 2 + 1, height + 1)

if __name__ == "__main__":
    gh.run()
```
