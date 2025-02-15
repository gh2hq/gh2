# Helpers

<a name="print" href="#print">#</a> gh.**print**(*\*args*, *\*\*kw*) : any

Print output to file to debug.

```py
import gh2 as app

app.print(1)
app.print([1, 2, 3])
app.print(2, 3, {'hello': 1}, test="test")
```

<a name="check_params" href="#check_params">#</a> gh.**check_params**()

Checks the type of params to output the potential error.

```py
import gh2 as gh

gh.full_screen()
gh.check_params()

gh.arc(0, 0, 0, 0, 'a', 'b')
gh.circle(0, 0, 'c')
gh.ellipse(0, 0, 'c', 'c')
gh.line(0, 0, 'c', 'c')
gh.point('c', 1)
gh.quad(0, 0, 0, 0, 0, 'c', 'c', 0)
gh.rect(0, 0, 0, 'c')
gh.square(0, 0, 'c')
gh.triangle(0, 0, 0, 0,  0, 'c')
gh.ellipse_mode('c')
gh.rect_mode('c')
gh.stroke_weight('c')
gh.begin_shape('c')
gh.bezier_vertex(0, 0, 0, 0, 0, 'c')
gh.curve_vertex(0, 'c')
gh.end_shape('up')
gh.vertex(0, 'c')
gh.open_shape('c', 'c')
gh.bezier(0, 0, 0, 0, 0, 0, 0, 'c')
gh.bezier_point(0, 0, 0, 'c', 1)
gh.bezier_tangent(0, 0, 0, 0, 'c')
gh.curve(0, 0, 0, 0, 0, 0, 0, 'c')
gh.curve_point(0, 0, 0, 0, 'c')
gh.curve_tangent(0, 0, 0, 0, 'c')
gh.curve_tightness('c')
gh.translate(0, 'c')
gh.scale('0')
gh.shear_x('0')
gh.shear_y('0')
gh.image('a', 0, 0, 0, 0)
gh.image_mode('c')
gh.load_image(0)
gh.color_mode(gh.RGB)
gh.tint(' ', (1, 0))
gh.text(0, 0, 0)
gh.text_width(0)
gh.text_height(0)
gh.text_size(0.0)
gh.text_font(0)
gh.set_cursor('c', 0)
gh.color_mode(gh.RGB)
gh.background('c', (0, 0, ))
gh.fill('c', (0, 0, ))
gh.stroke('c', (0, ))
c = gh.CColor('c', (1,))
gh.lerp_color(c, c, 0.5)

gh.run()
```
  