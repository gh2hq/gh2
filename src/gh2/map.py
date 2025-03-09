def map(x, a, b, c, d):
    if (a == b):
        return (c + d) / 2
    return (x - a) / (b - a) * (d - c) + c
