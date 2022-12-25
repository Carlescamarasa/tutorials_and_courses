def area(length=0, height=0, type=""):
    type = type.upper()
    if type == "T":
        surface = (length * height) / 2
    elif type == "S":
        surface = length ** 2
    elif type == "R":
        surface = length * height
    else:
        print("Input not supported.")
        return

    return surface

surface = area()

type = input("Type S (square), R (rectangle) or T (Triangle): ")
length = int(input("What length has the figure? "))
height = int(input("What height has the figure? "))
unit = input("What unit are you using? ")

surface = area(length=length, height=height, type=type)
print(f"El area es {surface} sq. {unit}")
