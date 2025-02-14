# Hand Pie Chart

There is a pie chart for mock data about the proportion of the population of different races. [[source](../../examples/pie.py)]

![preview.md](https://raw.githubusercontent.com/charming-art/public-files/master/example_piechart.png)

```py
import lighght as gh
from scales import scale_linear, scale_ordinal


def stack(data):
    values = []
    pre = 0
    for d in data:
        d['start'] = pre
        d['end'] = pre + d['value']
        values.append(d)
        pre = d['end']
    return values


# prepare data
people = [
    {'name': 'white', 'value': 43},
    {'name': 'yellow', 'value': 41},
    {'name': 'black', 'value': 16},
]

data = stack(people)

gh.print(data)
theta = scale_linear(
    [0, people[-1]['end']],
    [-gh.HALF_PI, gh.TWO_PI - gh.HALF_PI]
)
color = scale_ordinal(list(map(lambda x: x['name'], data)), [
    gh.CColor(('🖐🏻', 2),  (91, 143, 249), (91, 143, 249)),
    gh.CColor(('🖐️', 2), (97, 221, 170), (97, 221, 170)),
    gh.CColor(('🖐🏿', 2), (255,107,59), (255,107,59)),
])


# environment
gh.full_screen(gh.DOUBLE)
gh.color_mode(gh.RGB)
gh.no_cursor()

# draw
gh.translate(gh.get_width() / 2, gh.get_height() / 2)
for d in data:
    gh.no_stroke()
    gh.fill(color(d['name']))
    gh.arc(0, 0, 18, 18, theta(d['start']), theta(d['end']), gh.PIE)

gh.run()
```
