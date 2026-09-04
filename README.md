# Drawing Machine 🐢🖋

A Python turtle graphics project that lets you instruct a virtual turtle to draw amazing shapes and patterns!

## Description

Drawing Machine is an interactive turtle graphics application that brings creativity to life. Control a virtual turtle pen with simple commands to create beautiful drawings, geometric patterns, and artistic designs. Perfect for learning programming concepts like loops, functions, and coordinate systems.

## Features

✨ **Interactive Drawing** - Control a turtle pen with intuitive commands
📐 **Geometric Shapes** - Draw circles, squares, polygons, and more
🎨 **Customizable Styling** - Change pen color, width, and speed
🔄 **Repetitive Patterns** - Create complex designs with loops and recursion
📝 **Script-Based** - Write drawing instructions in Python
🎯 **Educational** - Learn programming through visual creativity

## Getting Started

### Prerequisites

- Python 3.x
- turtle module (included with Python)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/pg-141-mc/drawing-machine.git
cd drawing-machine
```

2. Run the drawing machine:
```bash
python drawing_machine.py
```

## Usage

Create your own drawings by writing Python scripts that instruct the turtle. Here are some basic commands:

```python
from turtle import *

# Move forward
forward(100)

# Turn right
right(90)

# Turn left
left(90)

# Change pen color
pencolor('red')

# Change pen width
penwidth(2)

# Draw a circle
circle(50)

# Lift pen (don't draw)
penup()

# Put pen down (draw)
pendown()
```

### Example: Draw a Square

```python
from turtle import *

for i in range(4):
    forward(100)
    right(90)

done()
```

### Example: Draw a Star

```python
from turtle import *

for i in range(5):
    forward(100)
    right(144)

done()
```

## Project Structure

```
drawing-machine/
├── README.md
├── drawing_machine.py
└── examples/
    ├── square.py
    ├── star.py
    └── patterns.py
```

## Tips for Creating Drawings

- **Use loops** to repeat commands efficiently
- **Use functions** to organize complex shapes
- **Experiment with colors** to make designs more vibrant
- **Adjust speed** with `speed()` for slower/faster drawing
- **Use coordinates** with `goto()` for precise positioning

## Learning Resources

- [Python Turtle Documentation](https://docs.python.org/3/library/turtle.html)
- [Turtle Graphics Tutorial](https://realpython.com/beginners-guide-to-python-turtle/)

## Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Suggest new features
- Add example drawings
- Improve documentation

## License

This project is open source and available for educational use.

## Author

Created by pg-141-mc 🎨

---

Happy drawing! 🐢✏️
