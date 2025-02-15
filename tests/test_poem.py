import gh2 as gh


def test_empty_poem():
    p = gh.poem()
    assert p.content() == ""


def test_single_point():
    p = gh.poem()
    p.point(0, 0, "x")
    assert p.content() == "x\n"


def test_multiple_points():
    p = gh.poem()
    p.point(0, 0, "a")
    p.point(1, 0, "b")
    p.point(0, 1, "c")
    p.point(1, 1, "d")
    expected = (
        "ab\n"
        "cd\n"
    )
    assert p.content() == expected


def test_sparse_points():
    p = gh.poem()
    p.point(0, 0, "x")
    p.point(2, 1, "y")
    expected = (
        "x  \n"
        "  y\n"
    )
    assert p.content() == expected


def test_margins():
    p = gh.poem()
    p.point(0, 0, "x")
    p.margin(left=2, top=1, bottom=1)
    expected = (
        "\n"
        "  x\n"
        "\n"
    )
    assert p.content() == expected


def test_overlapping_points():
    p = gh.poem()
    p.point(0, 0, "a")
    p.point(0, 0, "b")
    # Should keep the last character placed at each position
    assert p.content() == "b\n"


def test_zero_margins():
    p = gh.poem()
    p.point(0, 0, "x")
    p.margin(left=0, top=0, bottom=0)
    assert p.content() == "x\n"


def test_large_margins():
    p = gh.poem()
    p.point(0, 0, "x")
    p.margin(left=3, top=2, bottom=2)
    expected = "\n\n   x\n\n\n"
    assert p.content() == expected


def test_wide_poem():
    p = gh.poem()
    p.point(0, 0, "a")
    p.point(5, 0, "b")
    expected = "a    b\n"
    assert p.content() == expected


def test_tall_poem():
    p = gh.poem()
    p.point(0, 0, "a")
    p.point(0, 3, "b")
    expected = (
        "a\n"
        " \n"
        " \n"
        "b\n"
    )
    assert p.content() == expected
