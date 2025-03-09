# Mandelbrot Set

:::python fit

```py
import gh2 as gh

cols = 80
rows = 30
maxIter = 80

poem = gh.poem()

for x0 in range(cols):
    for y0 in range(rows):
        x = gh.map(x0, 0, cols, -2, 1)
        y = gh.map(y0, 0, rows, -1.164, 1.164)
        [a, b, i] = [0, 0, 0]
        while (i < maxIter):
            [a, b] = [a ** 2 - b ** 2 + x, 2 * a * b + y]
            if (a ** 2 + b ** 2) > 4:
                break
            i += 1
        ch = i == maxIter and "0" or " "
        poem.point(x0, y0, ch)

poem.print()
```

:::
