### Sets ###
""""""

my_set = set()
my_other_set = {} # Inicialmente es un dicionario si le metes datos pasa a ser sets

print(type(my_set))
print(type(my_other_set)) 

my_other_set = {"Felipe", "Calderón", 32} # esto ya es un sets ya que tiene datos
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Pipe")

print(my_other_set)
"""Un sets no es una estructura ordenada"""

my_other_set.add("Pipe")

print(my_other_set)
"""Un set no admite repetidos"""

print("Pipe" in my_other_set) #### Con esto verificamos si se encuentra en el sets la información
print("pipo" in my_other_set)

my_other_set.remove("Pipe") # Con esto eliminas lo que este en el sets
print(my_other_set) 

my_other_set.clear()
print(len(my_other_set))

del my_other_set
""" del my_other_set # con esto te cargas la propiedad
    print(my_other_set)
"""
my_set = {"Felipe", "Calderón", 32}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"list", "Swift", "Python", "Java"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"JavaScrip", "C#"}))# Los elementos JavaScript y C# solo se ejecutan en esta linea de codigo

print(my_new_set.difference(my_set)) # Con Difference saca los elementos de my_set y solo mostrando my_other_set
