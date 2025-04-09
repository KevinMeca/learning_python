
# https://www.python.org/

# Nomenclatura para variables en Python:
# - Usar nombres en minúsculas
# - Separar palabras con guiones bajos (_)
# - Los nombres deben ser descriptivos
# - No usar caracteres especiales o números al inicio
# - No usar palabras reservadas de Python
# Ejemplos correctos: mi_variable, nombre_usuario, contador_total
# Ejemplos incorrectos: miVariable, Contador, 1variable, class

# comentario en una linea

"""
comentario en 
varias lineas
"""

'''
Esto tambien 
es un comentario 
en varias lineas
'''

"""  
Las principales palabras reservadas (keywords) en Python son:
1.Control de flujo:
 - if, else, elif
 - for, while
 - break, continue
 - pass
2.Definición de funciones y clases:
 - def (para definir funciones)
 - class (para definir clases)
 - return (para retornar valores de funciones)
 - yield (para crear generadores)
3.Operadores lógicos:
 - and, or, not
 - in, is
4.Manejo de excepciones:
 - try, except, finally
 - raise
5.Importación y módulos:
 - import, from, as
6.Variables y constantes:
 - True, False
 - None
7.Control de acceso:
 - global, nonlocal
8.Lambdas:
 - lambda
9.Delimitadores:
 - with (para manejo de contextos)
10.Aserciones:
 - assert 
 Es importante mencionar que estas palabras son sensibles a mayusculas y minisculas, por
 lo que True es una palabra reservada (keyword) y true no lo es.
"""
my_variable = "Hola"
my_variable2 = "Mundo"

my_variable3 = 10
my_variable3 = 20

print(my_variable3)

"""
En Python, técnicamente no existen las constantes como en otros lenguajes de programación
(como C++ o Java). Sin embargo, hay convenciones y técnicas para implementar
valores constantes. Estas son las diferentes formas:

1.Convención por Nomenclatura:
   - La forma más común es usar nombres en MAYÚSCULAS para indicar que una variable es una constante
   - Es una convención entre programadores, pero técnicamente el valor puede ser modificado """
  
PI = 3.14159
MAX_CONNECTIONS = 100
DATABASE_URL = "https://ejemplo.com/db"
 
""""
2.Usando `enum.Enum`:
   - Es una forma más formal de crear constantes
   - Los valores son inmutables una vez definidos"""
  
from enum import Enum
   
class Colores(Enum):
       ROJO = "#FF0000"
       VERDE = "#00FF00"
       AZUL = "#0000FF"

"""
3.Usando `dataclasses` con `frozen=True`:
   - Crea una clase inmutable donde los valores no pueden ser modificados
   from dataclasses import dataclass """
   
@dataclass(frozen=True)
class Configuracion:
    API_KEY: str = "abc123"
    MAX_USUARIOS: int = 100
   
"""
4.Usando `typing.Final`:
   - Es una anotación de tipo que indica que una variable no debe ser reasignada
   - Es principalmente para documentación y herramientas de tipo """
   
from typing import Final
   
MAX_INTENTOS: Final = 3
   

"""La forma más común y recomendada es usar la convención de MAYÚSCULAS, ya que:
1. Es simple y clara
2. Es ampliamente reconocida en la comunidad Python
3. Es fácil de leer y entender
4. No requiere importaciones adicionales 

Por ejemplo: """

# Constantes matemáticas
PI = 3.14159
E = 2.71828

# Constantes de configuración
MAX_CONEXIONES = 100
TIEMPO_TIMEOUT = 30

# Constantes de rutas
RUTA_BASE = "/home/usuario/proyecto"
ARCHIVO_LOG = "app.log"

"""
Es importante notar que aunque estas variables están en mayúsculas, técnicamente 
aún pueden ser modificadas. La convención de mayúsculas es principalmente 
para indicar a otros programadores que no deben modificar estos valores. 
Si se necesita una verdadera inmutabilidad, se debería usar `enum.Enum` 
o `dataclasses` con `frozen=True`.
"""
"""
Tipos de datos primitivos en Python:

1. `int`: Números enteros (ej: 1, 100, -5)
2. `float`: Números decimales (ej: 3.14, 0.0, -2.5)
3. `str`: Cadenas de caracteres (ej: "Hola", "Python", "123")
4. `bool`: Booleanos (ej: True, False)
5. `None`: Tipo que representa la ausencia de valor
6. `list`: Listas (ej: [1, 2, 3], ["manzana", "banana", "cereza"])
    
"""

# Números
numero_entero = 42
numero_decimal = 3.14
numero_complejo = 1 + 2j

# Strings
texto = "Python es genial"
texto_multilinea = """Este es un texto
que ocupa varias líneas"""

# Booleanos
es_activo = True
tiene_permisos = False

# None
valor_vacio = None

# Bytes
datos_binarios = b'Hello World'

# Verificación de tipos
print(type(numero_entero))    # <class 'int'>
print(type(numero_decimal))   # <class 'float'>
print(type(texto))           # <class 'str'>
print(type(es_activo))       # <class 'bool'>












