# GH2 🚀

## ASCII Art Renderer for Python 🎨
Python class to generate and render ASCII art using a grid of characters (glyphs)

## Features 🔮
- Customizable Margins: Adjust top, bottom, and left margins for the generated art
- Glyph Placement: Place specific characters at coordinates within grid to form artwork
- Rendering: Stores art into string or prints to console based on margins and gylphs provided

## Installation 🛠️
To add to an existing project:
1. Clone repository into project directory `git clone https://github.com/gh2hq/gh2.git`
2. Install `npm install -e path/to/gh2`
3. All done!

## Usage 🎯
```python3
import gh2 
poem = gh2.poem()
poem.margin(top=0, bottom=0) #set margins for output (optional)

message = "I'm diagonal!" #message we want to display
for i, letter in enumerate(message): #iterate through message
    x,y=i,i
    poem.point(x,y,letter) #plots gylph on coordinate plane at (x,y)
poem.print() #print to console

'''
Or, conversely if you want to store as string and then print:
poem_as_string = poem.content() # store as string
print(poem_as_string)
'''
```
### Terminal Output 💻:
```
I            
 '           
  m          
             
    d        
     i       
      a      
       g     
        o    
         n   
          a  
           l 
            !
```
## Classes 📚
``_Poem``
The main class for creating and generating ASCII art (essentially the canvas)
- ``__init__()``: Initializes ASCII art object with empty list of glyphs and default margin values (0)
- ``margin(left=0, top=0, bottom=0)`` Sets margins for grid
- ``point(i,j,ch)`` Adds character to coordinates (i,j) on grid
- ``content()`` Returns gylphs and grid information into string
- ``print()`` Print ASCII art to console
