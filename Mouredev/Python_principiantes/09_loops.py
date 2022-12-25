### Loops ###

# While

my_condition = 0

while my_condition <  10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor que 10.")

print("La ejecución continúa.")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

# For
 
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 24, 62, 52, 30, 30, 17)

for element in my_tuple:
    print(element)

my_set = {35, 24, 62, 52, 30, 30, 17}
for element in my_set:
    print(element)


my_dict = {"Nombre":"Carles", "Apellido":"Camarasa", "Edad":"30"}
for element in my_dict.values():
    print(element)
else: # Es opcional
    print("El bucle ha finalizado.")