### Condicionales ###

my_condition = True 

if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta if")
    
my_condition = 5 * 2

if my_condition == 11: # Esto se ve si es True o False. Por ejemplo si es 10 el valor lo imprimiria
    print("Segundo if")
    
if my_condition != 11:
    print("Tercer if")
    
if my_condition > 10 and my_condition < 20: # También recuerda de los operadores logicos
    print("Es mayor que 10")
elif my_condition == 1:
    print("Es igual 1")
else:
    print("Es menor o igual que 10")
    
print("La ejecuciópn continua")
