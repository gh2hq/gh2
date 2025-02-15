# preview: https://raw.githubusercontent.com/charming-art/public-files/master/test_ccolor.png

import gh2 as gh

gh.full_screen()
gh.no_cursor()

c0 = gh.CColor()
c1 = gh.CColor('@')
c2 = gh.CColor('@', gh.RED)
c3 = gh.CColor('@', gh.RED, gh.YELLOW)

gh.stroke(c0)
gh.point(0, 0)  # nothing

gh.stroke(c1)
gh.point(1, 1)  # ('@', gh.WHITE, gh.BLACK)

gh.stroke(c2)
gh.point(2, 2)  # ('@', gh.RED, gh.BLACK)

gh.stroke(c3)
gh.point(3, 3)  # ('@', gh.RED, gh.YELLOW)

gh.run()
