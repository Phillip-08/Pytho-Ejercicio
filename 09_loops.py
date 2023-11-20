### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition +=2 # Suma la cantidad de dos en dos si fuera 1 sumaria de 1 en 1 #
    if my_condition == 10: # Es Optional 
        print("Mi número es 10")
else:
    print("Mi condición es mayor o igual que 10")
    
print("La ejecución sigue")
    
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break # Detiene la ejecución
    print(my_condition)
    
### For ###

my_list = [35, 24, 62, 52, 17]

for element in my_list:
    print(element)
    
my_dict = {
    "Nombre":"Felipe", 
    "Apellido":"Calderón", 
    "Edad":35, 
    "Lenguajes":{"Python", "Swift", "Java"},
    1:1.83,
    }

for i in my_dict.values():
    print(i)
    if i == "Edad":
        continue # No es recommended ocupar el continue ###
else:
    print("Buckle for a finalizado")