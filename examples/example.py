import michellespkg

# Calculate area of a rectangle
rect_area = michellespkg.area_rectangle(10, 5)
print(f"Area of rectangle: {rect_area}")

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
michellespkg.plot_triangle(base=8, height=4, origin=(1,1))