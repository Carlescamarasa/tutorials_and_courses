### Functions ###

def my_function ():
    print("Esto es una función.")
    
my_function ()

def sum_two_values (first_number, second_number):
    print(int(first_number) + int(second_number))

#sum_two_values(input("Primer número: "), input("Segundo número: "))

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return (10, 5)

print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Moure", name = "Brais")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts(input("Sí?"), input("Sí?"), input("Sí?"))