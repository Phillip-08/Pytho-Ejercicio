### Strings ###
# "len" sirve para contar caracteres


my_string = "Mi string"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "este es un string\ncon salto de linea" # "\n" da salto de linea
print (my_new_line_string)

my_tab_string = "\t Este es un String con tabulación" # "\t" es tabulacion y da un espacio grande antes de comenzar
print(my_tab_string)

""" Formateo """
name, surname, age = "Felipe", "Calderón", 35

print("Mi name is {} {} y mi edad es {}".format(name, surname, age))
print("Mi name is %s %s y mi edad es %d" %(name, surname, age)) #"%s" para string y "%d" para int, este es la forma más segura
print("Mi nombre es" + name+ "" + surname +"y mi edad es " + str(age))# esta no es la forma recomendada
print(f"Mi name is {name} {surname} y mi edad es {age}")# esta es la forma mas corta y segura

"""Desempaquetado de caracteres"""

language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

"""División"""

languaje_slice = language [1:3]
print(languaje_slice)

languaje_slice = language [1:]
print(languaje_slice)

languaje_slice = language [-2]
print(languaje_slice)

"""Reverse"""

reversed_languaje = language[::-1]
print(reversed_languaje)

"""Funciones"""

print(language.capitalize()) # Pone la primera letra en Mayuscula
print(language.upper())# Todo en Mayuscula
print(language.count("p")) # cuenta que letra hay por ejemplo la p, cuantas p hay y las cuenta
print(language.isnumeric())# ve si es numerico
print("1".isnumeric())
print(language.lower())# letras chicas
print(language.upper().isupper())# letras grandes
print(language.startswith("py"))# ve si empieza con lo indicado "py"

