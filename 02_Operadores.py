### Operadores ###
# suma, resta, dividir, etc.

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 9)

print("Hola" + "Python")
#print("Hola"-"Python") esto da error
#print("Hola" + "Python"+5) esto da error
print("Hola" + str(5)) #esto funciona ya que lo cambias a str
print("Hola" * 5) #esto funciona
print("Hola" * (5 ** 3)) #esto funciona

my_float = 2.5 * 2
print("Hola" * int(my_float)) # asi funciona ya que se pasa a int

# Operadores Comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 == 4)# Igual y igual
print(3 != 4)# Diferente

"""
En lo ejercicios de abajo no se cuentan caracteres
si ORDENACION ALFABETICA
"""
print("aaaa" > "abaa") # Ordenación alfabetica
print(len("aaaa") >= len("aaaa"))
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

###Operadodes Logicos 
### and, or y not

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 > 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))

