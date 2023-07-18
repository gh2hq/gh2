# Charming: Character Art Programming

Charming is a creative code language for character art programming.

## Installing

> TODO

## A Simple Example

```js
import * as cm from "@charming-art/charming";

const app = await cm.app({ mode: "double" });

for (let t = 0; t <= Math.PI * 2; t += Math.PI / 60) {
  const x = app.cols() / 2 + 10 * Math.cos(t) * Math.cos(t * 3);
  const y = app.rows() / 2 + 10 * Math.sin(t) * Math.cos(t * 3);
  app.stroke(cm.wide("🌟"));
  app.point(x, y);
}

document.body.append(app.render().node());
```

<img src="./img/star.png" width="100%" alt="star">

## API Reference

- [Creating Application](#creating-application)
- [Setting Attributes](#setting-attributes)
- [Drawing Shapes](#drawing-shapes)
- [Control Flow](#control-flow)
- [Getting Variables](#getting-variables)

### Creating Application

<a name="app" href="#app">#</a> cm.**app**(_options_)

```js
const app = await cm.app(options);
```

- **cols**
- **rows**
- **width**
- **height**
- **fontSize**
- **fontWeight**
- **fontFamily**
- **mode**

<a name="render" href="#render">#</a> app.**render**()

```js
app.render();
```

### Setting Attributes

<a name="scene" href="#scene">#</a> app.**scene**(_color_)

```js
app.scene("#000000");
```

<a name="scene" href="#stroke">#</a> app.**stroke**(_ch[, fg[, bg]]_)

```js
app.stroke("@", "steelblue", "orange");
```

<a name="wide" href="#wide">#</a> cm.**wide**(_ch_)

```js
cm.wide("🚀");
```

### Drawing Shapes

<a name="point" href="#point">#</a> app.**point**(_x, y_)

```js
app.point(0, 0);
```

<a name="pixels" href="#pixels">#</a> app.**pixels**(_x, y, render_)

```js
app.pixels(0, 0, (context) => {});
```

### Control Flow

<a name="each" href="#each">#</a> app.**each**(_data, iteratee_)

```js
app.each(data, (d, i, array) => {});
```

<a name="call" href="#call">#</a> app.**call**(_function[, arguments…]_)

```js
function draw(x, y) {}
app.call(draw, 0, 0);
```

### Getting Variables

For convince, apps provide methods to get some of internal variables.

<a name="node" href="#node">#</a> app.**node**()

Returns the canvas used to render the app. For example, to mount the rendered app to a specific DOM.

```js
const root = document.getElementById("id");
root.append(app.node());
```

<a name="cols" href="#cols">#</a> app.**cols**()

Returns the number of columns in the terminal. For example, to draw a point at the center of the terminal:

```js
app.point(app.cols() / 2, app.rows() / 2);
```

<a name="rows" href="#rows">#</a> app.**rows**()

Returns the number of rows in the terminal. For example, to draw a point at th center of the terminal:

```js
app.point(app.cols() / 2, app.rows() / 2);
```

<a name="width" href="#width">#</a> app.**width**()

Returns the computed width of the terminal, which satisfies the following constraint:

```js
app.width() === app.cols() * app.cellWidth();
```

<a name="height" href="#height">#</a> app.**height**()

Returns the computed height of the terminal, which satisfies the following constraint:

```js
app.height() === app.rows() * app.cellHeight();
```

<a name="cellWidth" href="#cellWidth">#</a> app.**cellWidth**()

Returns the computed width of the cells, which satisfies the following constraint:

```js
app.cellWidth() === app.width() / app.cols();
```

<a name="cellHeight" href="#cellHeight">#</a> app.**cellHeight**()

Returns the computed height of the cells, which satisfies the following constraint:

```js
app.cellHeight() === app.height() / app.rows();
```

<a name="fontSize" href="#fontSize">#</a> app.**fontSize**()

Returns the font size used to render text. For example, to get the default font size:

```js
const app = await cm.app();
app.fontSize(); // 15
```

<a name="fontWeight" href="#fontWeight">#</a> app.**fontWeight**()

Returns the font weight used to render text. For example, to get the default font weight:

```js
const app = await cm.app();
app.fontWeight(); // "normal"
```

<a name="fontFamily" href="#fontFamily">#</a> app.**fontFamily**()

Returns the font family used to render text. For example, to get the default font family:

```js
const app = await cm.app();
app.fontFamily(); // "courier-new, courier, monospace"
```
