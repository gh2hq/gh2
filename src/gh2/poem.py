class _Poem:
    def __init__(self):
        self.glyphs = []
        self.margin_top = 0
        self.margin_bottom = 0
        self.margin_left = 0

    def margin(self, left=0, top=0, bottom=0):
        self.margin_left = left
        self.margin_top = top
        self.margin_bottom = bottom
        return self

    def point(self, i, j, ch):
        self.glyphs.append((i, j, ch))
        return self

    def content(self):
        return _render(self.glyphs, self.margin_top,
                       self.margin_bottom, self.margin_left
                       )

    def print(self):
        output = self.content()
        print(output)
        return self


def _render(glyphs, margin_top, margin_bottom, margin_left):
    output = ""
    width, height = _sizeof(glyphs)
    matrix = _matrixof(glyphs, width, height)
    if margin_top > 0:
        output += "\n" * margin_top
    for i in range(height):
        if margin_left > 0:
            output += " " * margin_left
        for j in range(width):
            output += str(matrix[i][j][-1] if matrix[i][j] else " ")
        if i < height - 1:
            output += "\n"
    if margin_bottom > 0:
        output += "\n" * margin_bottom
    return output


def _sizeof(glyphs):
    if not glyphs:
        return 0, 0
    return max(glyphs, key=lambda x: x[0])[0] + 1, max(glyphs, key=lambda x: x[1])[1] + 1


def _matrixof(glyphs, width, height):
    matrix = [[[] for _ in range(width)] for _ in range(height)]
    for i, j, ch in glyphs:
        matrix[j][i].append(ch)
    return matrix


def poem():
    return _Poem()
