# Zeros

:::python fit

```py
import gh2 as gh

poem = gh.poem()

poem.margin(top=1, bottom=1)

for j in range(10):
    for i in range(20):
        if (i + j) % 2 == 1:
            poem.point(i, j, "0")

poem.print()
```

:::
