import gh2 as gh

# If you want to draw a ascii text, you'd
# better use raw string: r'''xxx'''.
head = r'''
         .-"""-.
        /       \
        \       /
 .-"""-.-`.-.-.<  _
/      _,-\ ()()_/:)
\     / ,  `     `|
 '-..-| \-.,___,  /
       \ `-.__/  /
        `-.__.-'`
'''

face = "(^O^)/"

gh.full_screen()
gh.no_cursor()

gh.stroke(fg=gh.RED, bg=gh.YELLOW)
gh.text(head, 0, 0)
gh.text(face, 25, 5)

gh.stroke_weight(1)
gh.text('h', 35, 5)

gh.run()