"""Lists"""

my_list = list()    #1 forma de lista
my_other_list = []  #2 forma de lista

print(len(my_list))

my_list = [35, 42, 50, 62, 91, 91]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.83, "Felipe", "Calderón"]

print(type(my_list))
print(type(my_other_list))
print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list.__len__()) # Puedes contar la cantidad que tiene la lista osea del objetos que tenga
#print(my_other_list[-5]) IndexError
#print(my_other_list[4]) IndexError

age, height, name, last_name = my_other_list
print(name)

print(my_list + my_other_list)
#print(my_other_list * my_list) Error

my_other_list.append("Alegría")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(91)
print(my_list)

print(my_list.pop(2)) # con el 2 es el indice que quieres eliminar, y sin nada elimina el ultimo
print(my_list)

del my_list[2] # con DEL eliminas la info del objetivo por indice
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2]) # con esto se puede hacer sup listas

"""
my_list = "Hola Python"
print(my_list)
print(type(my_list))

Con esto se rompe la lista anterior, ya que falta tipado de codigo de Python

"""
