width  = float(input("Veuillez saisir la largeur du rectangle  : "))
length = float(input("Veuillez saisir la longueur du rectangle : "))

area      = width * length
perimeter = (width + length) * 2

#print("La surface du rectangle est {} et le perimetre est {}".format(format(area, ".2f"), format(perimeter, ".2f")))
print(f"la surface du rectagle est {format(area, ".2f")} et le perimetre est {format(perimeter, ".2f")}")