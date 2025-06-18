# Getting Started

This guide will help you get started with the basic usage of `michellespkg`.

## Importing the Package

Once `michellespkg` is installed, you can import it and its components into your Python scripts or interactive sessions.

```python
# Example:
from michellespkg.shapes import Circle, Rectangle

circle = Circle(radius=5)
print(f"Circle Area: {circle.area()}")

rectangle = Rectangle(width=4, height=6)
print(f"Rectangle Area: {rectangle.area()}")
```

## Basic Example

Below is a simple example demonstrating how to use a core feature of `michellespkg`.

```python
import michellespkg

# Calculate area of a rectangle
rect_area = michellespkg.area_rectangle(10, 5)
print(f"Area of rectangle: {rect_area} ")

# Calculate area of a circle
circ_area = michellespkg.area_circle(7)
print(f"Area of circle: {circ_area}")

# Calculate area of a triangle
tri_area = michellespkg.area_triangle(8, 4)
print(f"Area of triangle: {tri_area}")

# Visualize a rectangle
michellespkg.plot_rectangle(length=10, width=5)

# Visualize a circle
michellespkg.plot_circle(radius=7, center=(2, 2))

# Visualize a right-angled triangle
michellespkg.plot_triangle(base=8, height=4, origin=(1, 1))
```

Refer to the [API Reference](../api.md) for more detailed information on available modules and functions.