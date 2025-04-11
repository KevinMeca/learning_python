#Operadores y estructuras de Control

#Operadores arimeticos
print(f"suma: 10+3:{10+3}")
print(f"resta: 10-3:{10-3}")
print(f"multiplicacion: 10*3:{10*3}")
print(f"division: 10/3:{10/3}")
print(f"division entera: 10//3:{10//3}")
print(f"modulo: 10%3:{10%3}")
print(f"potencia: 10**3:{10**3}")

#operadores de comparacion  
print(f"igual: 10==3:{10==3}")
print(f"diferente: 10!=3:{10!=3}")
print(f"mayor: 10>3:{10>3}")
print(f"menor: 10<3:{10<3}")
print(f"mayor o igual: 10>=3:{10>=3}")
print(f"menor o igual: 10<=3:{10<=3}")

#operadores logicos
print(f"AND &&: 10>3 and 10<20:{10>3 and 10<20}")
print(f"OR ||: 10>3 or 10<20:{10>3 or 10<20}")
print(f"NOT !: not 10>3:{not 10>3}")

#operadores de asignacion
my_variable = 15
print(my_variable)
my_variable += 3   #suma y asignacion
print(my_variable)
my_variable -= 3  #resta y asignacion
print(my_variable)
my_variable *= 3  #multiplicacion y asignacion
print(my_variable)
my_variable /= 3  #division y asignacion
print(my_variable)
my_variable //= 3  #division entera y asignacion
print(my_variable)
my_variable %= 3  #modulo y asignacion
print(my_variable)
my_variable **= 3  #potencia y asignacion
print(my_variable)

#operadores de identidad (compara si son el mismo objeto)
my_variable = 15
my_variable2 = 15
my_variable3 = 30
print(f"identidad: my_variable is my_variable2:{my_variable is my_variable2}")
print(f"identidad: my_variable is my_variable3:{my_variable is my_variable3}")

#operadores de pertenencia (compara si un elemento esta en una secuencia)
my_list = [1,2,3,4,5]
print(f"pertenencia: 1 in my_list:{1 in my_list}")
print(f"pertenencia: 1 not in my_list:{1 not in my_list}")


#operadores de bit
my_variable = 10 #1010
my_variable2 = 30 #11110
print(f"AND: my_variable & my_variable2:{my_variable & my_variable2}") #1010
print(f"OR: my_variable | my_variable2:{my_variable | my_variable2}") #11110    
print(f"XOR: my_variable ^ my_variable2:{my_variable ^ my_variable2}") #10000
print(f"NOT: ~my_variable:{~my_variable}")

'''
Estructura de control
'''
#condicionales
#if
my_variable = 10
if my_variable > 0:
    print("my_variable es mayor que 0")
else:
    print("my_variable es menor que 0")

#elif
my_variable = 10
if my_variable > 0:
    print("my_variable es mayor que 0")
elif my_variable == 0:
    print("my_variable es igual a 0")
else:
    print("my_variable es menor que 0")

#switch
my_variable = 10
match my_variable:
    case 1:
        print("my_variable es igual a 1")
    case 2:
        print("my_variable es igual a 2")
    case _:
        print("my_variable no es igual a 1 o 2")

#iteraciones
#ciclos
#for
for i in range(1,11):
    print(i)    

#while
i = 1
while i <= 10:
    print(i)
    i += 1  

#break
for i in range(1,11):
    if i == 5:
        break
    print(i)    

#continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)        

#funciones
#def
def my_function():
    print("Hello, World!")

my_function()

#return
def my_function():
    return "Hello, World!"

print(my_function())

#lambda
my_lambda = lambda x: x*2
print(my_lambda(10))

#map
my_list = [1,2,3,4,5]

#manejo de excepciones
try:
    my_variable = 10/0
except ZeroDivisionError:
    print("Error: Division por cero")   
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Fin del programa") 







