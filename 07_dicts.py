### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Felipe", "Apellido":"Calderón", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Felipe", 
    "Apellido":"Calderón", 
    "Edad":35, 
    "Lenguajes":{"Python", "Swift", "Java"},
    1:1.83,
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"]= "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Pipe"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Lenguajes" in my_dict) #### Con esto verificamos si se encuentra por clave, no busca por el contenido
print("Felipe" in my_dict)

print(my_dict["Nombre"]) # Con esto tienes la info del indice

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict =dict.fromkeys(("Nombre", 1))# Crea un nuevo dicionario sin valores y recuerda que hay otra forma pero esta es la correcta
print(my_new_dict)

my_new_dict =dict.fromkeys(my_dict)# con esto aprovechas los indices del dicionario, es como una copia
print(my_dict)
