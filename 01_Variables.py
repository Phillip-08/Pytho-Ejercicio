# Variables

my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print (my_int_variable)

my_bool_variable = False
print (my_bool_variable)

# Con cadenacion de variables
print (my_variable, my_int_variable, my_bool_variable)
""" 
Con el "str" puedes transformar un numero ("int") 
lo puedes trasformar a Strind "str" 
"""
#Ejemplo
my_int_to_str_variable = str(my_int_variable)
print (my_int_to_str_variable)
print (type(my_int_to_str_variable))

# Función del sistema Ej. len, str, etc.
print (len(my_int_to_str_variable))

# Variables de una sola linea
name, surname, alias, age = "Felipe", "Calderón", "Pipe", "32"
# Esto "no" es una buena practica
print ("Mi nombre es: ", name, surname, "mi edad: ", age, "mi alias es: ", alias )

# ingreso de input
"""first_name = input("Cual es tu nombre: ")
age = input("Que edad tienes: ")

print (first_name)
print (age)

"""
# ¿Forzamos el Tipo?
address: str = "Mi dirección"
address = 32
print(type(address))

