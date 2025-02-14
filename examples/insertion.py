from random import shuffle
import lighght as gh

sorted = None
j = 0
cards = [
    '🀇', '🀈', '🀉', '🀊', '🀋', '🀌', '🀍', '🀎', '🀏',
    '🀐', '🀑', '🀒', '🀓', '🀔', '🀕', '🀖', '🀗', '🀘',
    '🀙', '🀚', '🀛', '🀜', '🀝', '🀞', '🀟', '🀠', '🀡',
]


def generate_data():
    data = []
    for i in range(len(cards)):
        data += [i]
    shuffle(data)
    return data


def insertion_sort(data):
    sorted = [[d for d in data]]
    for i in range(1, len(data)):
        j = i - 1
        current = data[i]
        while j >= 0 and current < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
        sorted.append([d for d in data])
    return sorted


@gh.setup
def setup():
    gh.full_screen(gh.DOUBLE)
    gh.no_cursor()

    global sorted
    data = generate_data()
    sorted = insertion_sort(data)


@gh.draw
def draw():
    global j
    x = (gh.get_width() - len(sorted[0])) / 2
    y = (gh.get_height() - len(sorted)) / 2
    gh.translate(x, y)
    if j < len(sorted):
        numbers = sorted[j]
        for i, n in enumerate(numbers):
            gh.stroke(cards[n])
            gh.point(i, j)
        j += 1


gh.run()
