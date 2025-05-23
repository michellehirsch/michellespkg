"""
A collection of functions to calculate the area of common 2D shapes.
"""

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def area_rectangle(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.

    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

def area_circle(radius: float) -> float:
    """
    Calculates the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius ** 2

def area_triangle(base: float, height: float) -> float:
    """
    Calculates the area of a triangle.

    Args:
        base: The base length of the triangle.
        height: The perpendicular height of the triangle.

    Returns:
        The area of the triangle.

    Raises:
        ValueError: If base or height is negative.
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

def plot_rectangle(length: float, width: float, origin: tuple[float, float] = (0, 0)):
    """
    Visualizes a rectangle with its dimensions.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
        origin: The (x, y) coordinates of the bottom-left corner. Defaults to (0,0).

    Raises:
        ValueError: If length or width is not positive.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive for visualization.")

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal', adjustable='box')

    rect_patch = patches.Rectangle(origin, length, width, linewidth=1, edgecolor='r', facecolor='lightcoral', alpha=0.6)
    ax.add_patch(rect_patch)

    # Add dimension labels
    center_x = origin[0] + length / 2
    ax.text(center_x, origin[1] - 0.05 * width, f'Length: {length}', ha='center', va='top', fontsize=9)
    center_y = origin[1] + width / 2
    ax.text(origin[0] - 0.05 * length, center_y, f'Width: {width}', ha='right', va='center', rotation='vertical', fontsize=9)

    # Set plot limits with padding
    padding_x = length * 0.25
    padding_y = width * 0.25
    ax.set_xlim(origin[0] - padding_x, origin[0] + length + padding_x)
    ax.set_ylim(origin[1] - padding_y, origin[1] + width + padding_y)

    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title(f"Rectangle (L={length}, W={width})")
    plt.grid(True)
    plt.show()

def plot_circle(radius: float, center: tuple[float, float] = (0, 0)):
    """
    Visualizes a circle with its dimensions.

    Args:
        radius: The radius of the circle.
        center: The (x, y) coordinates of the circle's center. Defaults to (0,0).

    Raises:
        ValueError: If radius is not positive.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive for visualization.")

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal', adjustable='box')

    circle_patch = patches.Circle(center, radius, linewidth=1, edgecolor='b', facecolor='lightblue', alpha=0.6)
    ax.add_patch(circle_patch)

    # Add dimension label (radius line and text)
    ax.plot([center[0], center[0] + radius * math.cos(math.pi/4)], 
            [center[1], center[1] + radius * math.sin(math.pi/4)], 'k--')
    ax.text(center[0] + radius * 0.5 * math.cos(math.pi/4), 
            center[1] + radius * 0.5 * math.sin(math.pi/4) + radius*0.05, 
            f'Radius: {radius}', ha='center', va='bottom', fontsize=9)

    # Set plot limits with padding
    padding = radius * 0.25
    ax.set_xlim(center[0] - radius - padding, center[0] + radius + padding)
    ax.set_ylim(center[1] - radius - padding, center[1] + radius + padding)

    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title(f"Circle (R={radius})")
    plt.grid(True)
    plt.show()

def plot_triangle(base: float, height: float, origin: tuple[float, float] = (0, 0)):
    """
    Visualizes a right-angled triangle with its dimensions.
    The origin is the vertex of the right angle.
    The base extends along the positive x-axis from the origin.
    The height extends along the positive y-axis from the origin.

    Args:
        base: The base length of the triangle.
        height: The perpendicular height of the triangle.
        origin: The (x, y) coordinates of the right-angle vertex. Defaults to (0,0).

    Raises:
        ValueError: If base or height is not positive.
    """
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive for visualization.")

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal', adjustable='box')

    v0 = origin
    v1 = (origin[0] + base, origin[1])
    v2 = (origin[0], origin[1] + height)
    triangle_patch = patches.Polygon([v0, v1, v2], linewidth=1, edgecolor='g', facecolor='lightgreen', alpha=0.6)
    ax.add_patch(triangle_patch)

    # Add dimension labels
    ax.text(origin[0] + base / 2, origin[1] - 0.05 * height, f'Base: {base}', ha='center', va='top', fontsize=9)
    ax.text(origin[0] - 0.05 * base, origin[1] + height / 2, f'Height: {height}', ha='right', va='center', rotation='vertical', fontsize=9)

    # Set plot limits with padding
    padding_x = base * 0.25
    padding_y = height * 0.25
    ax.set_xlim(origin[0] - padding_x, origin[0] + base + padding_x)
    ax.set_ylim(origin[1] - padding_y, origin[1] + height + padding_y)

    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title(f"Right-Angled Triangle (B={base}, H={height})")
    plt.grid(True)
    plt.show()