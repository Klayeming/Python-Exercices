"""
Module: Rectangle Geometry Calculator

Calculates the perimeter and area of a rectangle.

Formulas:
  - Area: length × width
  - Perimeter: 2 × (length + width)
"""

width = float(input("Veuillez saisir la largeur du rectangle  : "))
length = float(input("Veuillez saisir la longueur du rectangle : "))

# Calculate area and perimeter
area = width * length
perimeter = (width + length) * 2

print(f"La surface du rectangle est {format(area, '.2f')} et le perimetre est {format(perimeter, '.2f')}")