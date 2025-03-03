# Information

:::python fit

```py
import gh2 as gh

char = 'INFORMATION'
n = len(char)

poem = gh.poem()

poem.margin(top=1, bottom=1)

for j in range(n):
    for i in range(n * 2 - 1):
        ch = char[j] if j == i / 2 else "."
        poem.point(i, j, ch)

poem.print()
```

:::
