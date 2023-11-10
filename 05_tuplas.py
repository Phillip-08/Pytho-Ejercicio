### Tuples ###

# Estos son contructores muy parecidos pero hay que pasar tuple o list pero se diferencia con () o []
"""Las tuplas son valores imutables o sea no te deja cambiarlo y no te deja ingresar más datos"""

my_tuple = tuple()  #Esta es una forma de escribir tuplas 1
my_other_tuple = () #Esta es una forma de escribir tuplas 2

my_tuple = (35, 1.83, "Felipe", "Calderón")
my_other_tuple = ()

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Calderón"))
print(my_tuple.index("Calderón"))

#my_tuple[1] = 1.70 error 
"""my_tuple[1] = 1.70 "" no se puede isertar debido que la tupla es inmutable"""

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple [3:6])

"""Cambiar a lista"""
my_tuple = list(my_tuple)
print(type(my_tuple))
"""Isercion en la lista"""
my_tuple[3] = "Alegría"
my_tuple.insert(1, "Azul")
"""Cambiar a lista"""

"""Cambiar a Tupla nuevamente"""
my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

#del my_tuple[2] esto es un error ya que hacer inmutable no te dejara eliminar parte de la tupla
""" "Del" elimina la tupla y no deveria hacerlo ya que es inmutable un error de python"""
"""del my_tuple
print(my_tuple)"""