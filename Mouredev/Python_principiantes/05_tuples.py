### Tuples ###

my_tuple = tuple()
my_other_tuple = ()
x = 35
my_tuple = (x, 1.77, "Brais", "Moure", "Brais")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) Error
#print(my_tuple[-6]) Error

print(my_tuple.count("Brais"))

print(my_tuple.index("Moure"))

print(my_tuple.index("Brais"))