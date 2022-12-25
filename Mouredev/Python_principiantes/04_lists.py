### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(type(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_other_list)) 

print(type(my_list))
print(type (my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4]
)
print(my_list.count(30))

#print(my_other_list())
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list [2],  my_other_list [1],  my_other_list [0],  my_other_list [3]

print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list) Error

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

del my_list[2]
print(my_list)

my_list.remove(30)
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

my_new_list = my_list.copy()

my_list.clear()
my_new_list.sort()
print(my_list)
print(my_new_list)

#my_list = list("Hola Python")
#print(my_list)
