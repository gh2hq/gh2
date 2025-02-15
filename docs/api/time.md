# Time

Methods for returning information about current time.

<a name="day" href="#day">#</a> gh.**day**()

Returns the current day as a value from 1 - 31.

<a name="hour" href="#hour">#</a> gh.**hour**()

Returns the current hour as a value from 0 - 23.

<a name="millis" href="#millis">#</a> gh.**millis**()

Returns the number of milliseconds (thousandths of a second) since starting the program.

<a name="minute" href="#minute">#</a> gh.**minute**()

Returns the current minute as a value from 0 - 59.

<a name="month" href="#month">#</a> gh.**month**()

Returns the current month as a value from 1 - 12.

<a name="second" href="#second">#</a> gh.**second**()

Returns the current second as a value from 0 - 59.

<a name="year" href="#year">#</a> gh.**year**()

Returns the current year as an integer (2003, 2004, 2005, etc).
  
```py
import gh2 as gh


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()


@gh.draw
def draw():
    gh.background(' ')
    date = f'{gh.year()} . {gh.month()} . {wrap(gh.day())}'
    time = f'{wrap(gh.hour())} : {wrap(gh.minute())} : {wrap(gh.second())}'

    gh.text_align(gh.CENTER)
    gh.text_size(gh.BIG)
    h1 = gh.text_height(date)
    h = h1 + 10

    gh.translate(gh.get_width() / 2, (gh.get_height() - h) / 2)
    gh.text(date, 0, 0)
    gh.text(time, 0, 10)


def wrap(n):
    return f'0{n}' if n < 10 else n


gh.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_time.gif" />