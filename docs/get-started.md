# Get Started

## Try gh2 online

You can try VitePress directly in your browser on gh's [Online Eidtor](https://editor.gh2.dev/).

## Install from PyPI 🛠️

```sh
$ pip install gh2
```

## Usage 🎯

:::python

```py
import gh2 as gh

poem = gh.poem()

# Sets margins for output (optional).
poem.margin(top=1, bottom=1)

# The message we want to display.
message = "Hello, gh2!"

# Iterates through message.
for i, letter in enumerate(message):
    # Plots gylph on coordinate plane at (x, y).
    poem.point(i, i, letter)

# Prints to console.
poem.print()
```

:::

Or, conversely if you want to store as string and then print:

```py
# Stores as string.
string = poem.content()
print(string)
```
