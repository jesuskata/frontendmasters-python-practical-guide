# Frontendmasters: Practical Guide to Python

<!-- TOC -->
* [Frontendmasters: Practical Guide to Python](#frontendmasters--practical-guide-to-python)
  * [Notas](#notas)
  * [Variables and Data Types](#variables-and-data-types)
<!-- TOC -->

## Notas

- Aquí está la url del contenido del curso: [learnpython](https://practical.learnpython.dev/).
- REPL: Read Evaluate Print Loop. Puedes considerarlo más tu área de bosquejo, donde puedes probar y experimentar con tu código de Python.
- Puedes escribir en la consola de Python `import this` y obtendrás los 19 principios de Python.
- Hay un par de comandos _easter egg_ que puedes obtener escribiendo: `from __future__ import braces` y `import antigravity`.
- Normalmente el punto de entrada de un programa de Python está en `"__main__"`, es por eso que verás en cada programa la siguiente línea de código `if __name__ = "__main__:"`, que es donde Python comenzará a correr el código que escribiste.

## Variables and Data Types

- Es importante recordar que Python es un lenguaje dinámico, esto quiere decir que no tienes que decirle a Python el tipo de lo que estás escribiendo.
- Cuando crees variables, debes ser lo más explícito posible al nombrar las variables.
- Para Python se definen las variables de acuerdo a la convención `snake_casing`.
- Es importante saber que no puedes definir una variable que comience con número y tener cuidado de no usar `special keywords`(palabras reservadas) de Python al nombrar variables.
- Puedes acceder al listado de palabras reservadas escribiendo en la consola de Python `help()` y después `keywords`, y obtendrás la siguiente lista:

Here is a list of the Python keywords.  Enter any keyword to get more help.

|Palabra|Palabra  |Palabra  |Palabra  |Palabra|
|-------|---------|---------|---------|-------|
| False | await   | else    | import  | pass  |
| None  | break   | except  | in      | raise |
| True  | class   | finally | is      | return|
| and   | continue| for     | lambda  | try   |
| as    | def     | from    | nonlocal| while |
| assert| del     | global  | not     | with  |
| async | elif    | if      | or      | yield |

- Los tres métodos REPL que más uso darás en tu carrera como programador Python son: `help()` (te da una ayuda de Python), `type()` (te devuelve el tipo de lo que introduzcas como parámetro) y `dir()` (te devuelve un listado de todos los métodos disponibles de lo que introduzcas como parámetro).
- En los cálculos con valores numéricos, al hacer `25 / 5` te devolverá un tipo `float`, pero puedes evitarlo haciéndo el cálculo de la siguiente manera `25 // 5` y te devolverá el resultado como `int`.
- Para los strings, es recomendable usar `double quotes`, de esta forma al usar algo como `don't...` no tendrás errores en la consola y tus variables siempre estarán escritas de la misma forma (con comillas dobles).
- Si vas a escribir un string largo, se puede usar `""""` para definirlo, cerrando de la misma forma con tres comillas dobles.
- Puedes concatenar strings con el símbolo `+`.
- Puedes usar una `f` al inicio de un string, y de esta forma puedes agregar variables y/o expresiones a tu string, lo que te permite agregarle el valor de tus variables. Ejemplo:

```python
a = 37
f"Mi edad es de {a} años" # Mi edad es de 37 años
```

- Se puede declarar una lista con `[]` o con `list()`

## Functions, Loops and Logic

### Tuples

- Son pequeñas colecciones en las que puedes poner diferentes tipos de items. A diferencia de las listas que son usadas generalmente para contener tipos similares de items, las tuplas no tienen restricciones en esa área.
- Otra diferencia entre las listas y las tuplas es que las tuplas son `inmutables`.
- Las listas son creadas con `[]`, pero las tuplas son creadas con `()`.
- Para que una tupla de un solo elemento sea de tipo tupla, debe cumplir con la condición de tener una coma después del elemento `(1,)`.
- Se puede hacer una extracción de valores y asignarlos en una variable de la siguiente manera:

```python
student = ("Jesús", 37, "History", 9.5)
name, age, subject, gpa = student
name # Jesús
age # 37
subject # History
gpa # 9.5
```

- Para lo anterior, se debe cumplir una condición importante, y es que las variables a definir deben cumplir con el número de índices dentro de la tupla.
- Se puede omitir el uso de alguno de los índices con `_`, por ejemplo, de acuerdo al código de arriba `name, age, subject, _ = student`, con esto el último valor no estará guardado en ninguna variable.

### Sets

- Son tipo mutable y solo te permiten contener tipos inmutables dentro y de manera desordenada.
- Otra característica es que son rápidos. Por lo mismo que están bien definidos y no contienen: lists, dictionaries, y otros tipos mutables.
- Para crear set puedes hacerlo con `{}` y con `set()`, pero como nota importante, no puedes crear un set vacío con `{}`, porque Python lo reconocería como un tipo `dict`, para crear un set vacío, lo puedes hacer con la instrucción `set()`.
- Set puede tener un solo ítem dentro o múltiples.
- Set no puede contener valores duplicados, por ejemplo si creo una variable `my_set = {3, 3, 4,}`, mi variable al llamarla será `{3, 4}`.
- Hay un tip para saber qué es mutable y qué no lo es con el método `hash()`:

```python
hash(5)
# 5
hash("Hello")
# -6361881465459099289
hash(["Hello"])
# Traceback (most recent call last):
#   File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#   File "<input>", line 1, in <module>
# TypeError: unhashable type: 'list'
```

- Puedes crear un set de un array existente y evitar los duplicados al mismo tiempo. Ejemplo:

```python
names = ["Aleisa", "Aleisa", "Tiana", "Jana"]
set(names)
# {'Jana', 'Tiana', 'Aleisa'}
```

### Dictionaries

- Es un tipo de dato mutable que nos permite guardar `key` y `value` emparejados.
- Como se mencionó arriba, son inmutables, pero el dictionary key debe ser inmutable, por qué, porque los `key` de los dictionaries deben ser `hashables`. De esta manera Python se asegura de realizar búsquedas rápidas.
- Los dictionaries se definen con `{}`, para crear un dict vacío, basta con escribir `{}`, y para crear uno con elementos debe cumplir la regla `{key: value}`.
- Puedes acceder a los valores del dict con la connotación `my_dict[key]`. Por ejemplo:

```python
my_dict = {"one": 1, "two": 2}
my_dict["one"]
# 1
```

- Pero no puedes acceder a un valor por "índice" `my_dict[0]`, porque la restricción es que se le indique el `key` para que sea válido.
- Hay tres métodos muy útiles que se usarán mucho con los dicts:

```python
my_dict = {"one": 1, "two": 2}
my_dict["three"] = 3
my_dict
# {'one': 1, 'two': 2, 'three': 3}
my_dict.keys()
# dict_keys(['one', 'two', 'three'])
my_dict.values()
# dict_values([1, 2, 3])
my_dict.items()
# dict_items([('one', 1), ('two', 2), ('three', 3)])
```

### Running Python files

- Recuerda que para nombrar variables como para nombrar archivos se hace con `lowercase`  y `snake_case`, además, a diferencia de los nombres de variables que deben ser muy descriptivos, los archivos deben ser de preferencia nombres cortos.
- Vas a encontrar de repente algunos archivos con extensión `pyc`, no te preocupes, son archivos para optimización, solo no hagas commit de ellos. En caso de que creas que hay algún `pyc` escondido y temes que se haga commit de él, prueba corriendo el siguiente comando `find . --name "*.pyc" --delete`.
- Para correr un programa de Python, asegúrate de estar en tu ambiente virtual y correr `python <file_name>`.
- Si quieres ver el resultado de tus programas, vas a tener que usar print para ver lo que deseas que se imprima en la terminal, solo evita hacer esto a nivel producción.
- Existe una librería dentro de python para imprimir de manera más legible, su nombre es `pretty print` y se usa `import pprint` y en vez de usar `print(...)` vas a usar `pprint(...)`.

### Functions, arguments, scopes

- Las funciones se definen `def my_func_name():`, es importante tener los dos puntos al final de la declaración, y todo lo que va dentro de la función debe ir con espacios para que vaya dentro de su contexto.
- Es importante considerar dejar un espacio después de terminar tu función, por cuestiones de lectura adecuada del programa.
- Las funciones deben retornar algo, en caso de que no lo hagas, al leer su tipo, tendrás como respuesta `NoneType`.
- Una función puede aceptar todos los argumentos que quieras, separados de comas, y esos argumentos serán usados dentro de la función para el propósito que quieres.
- Si al crear una función decides que uno de los argumentos puede no ir al llamar la función, pero deseas incluir un valor default, lo puedes hacer:

```python
def my_sum_func(x, y, z=1):
    return x + y + z

my_sum_func(5, 5)
# 11 porque z tiene un valor default de 1
my_sum_func(5, 5, 5)
# 15
```

- De acuerdo a lo anterior, entonces tenemos que existe un orden para la definición de una función con argumentos opcionales, primero van los argumentos requeridos y al final los argumentos opcionales.
- Puedes llamar a la función con los argumentos en desorden, siempre y cuando le digas a Python el valor específico de casa argumento para que pueda hacer la lectura adecuada:

```python
def my_sum_func(x, y, z=1):
    return x + y + z

my_sum_func(y=4, z=2, x=10)
# 16
```

- No ocupes argumentos mutables como default values en la definición de tu función, ya que no se comportarán de la manera en que probablemente esperas. Ejemplo:

```python
def do_stuff(list_two=[]):
    list_two.append("stuff!")
    return list_two

do_stuff()
# ['stuff!']
do_stuff()
# ['stuff!', 'stuff!']
do_stuff()
# ['stuff!', 'stuff!', 'stuff!']
```

- El scope de cada función le pertenece a cada variable que se defina dentro de la función y no afuera de ella. Ejemplo:

```python
name = "Alex"
print(f"Name OUTSIDE the function is: {name}")
# Name OUTSIDE the function is: Alex
def try_change_name():
    name = "Max"
    print(f"Name INSIDE the function is: {name}")
    
try_change_name()
# Name INSIDE the function is: Max
name
# 'Alex'
```

- Por lo tanto, no trates de querer cambiar una variable que fue definida fuera de la función, porque no será posible, aunque tienes acceso a ella y es muy útil (como usar una variable global `url` por ejemplo), el scope no es el mismo.
- Una recomendación es que si vas a definir una constante, la definas con `MAYUSCULAS_Y_SEPARADAS_CON_GUION_BAJO`.

### Boolean Logic and Control Statements

- `Thruthiness` evalúa una expresión si es `False` o `True`.
- Con los tipos `int` los `ceros` son `False` y todos los demás números incluidos los negativos son `True`.
- Para los otros tipos de valores como `list`, `tuple`, `set` y `dict` todos los contenedores vacíos son `False` y los que tienen al menos un elemento son evaluados como `True`. `None` siempre será `False`.
- Para hacer una evaluación puedes usar `bool()`, también con una expresión de comparación con `==` o `!=`.
- Puedes intentar validar si es verdad que dos listas son iguales, pero a continuación se muestra la forma incorrecta y correcta de hacerlo:

```python
list_one = [1, 2, 3]
list_two = [1, 2, 3]
list_one == list_two
# True
list_one is list_two # ¿Esta es la manera correcta de validar, porque checa la identidad, osea, esto apunta al mismo lugar en memoria?
# False

x = None
x is None
# True
[] is None
# False
```

- Igualmente se tienen `and`, `or`, `not`. Por ejemplo:

```python
a = True
b = True
a and b
# True
True and False
# False
True or False
# True
True or True
# True
False or False
# False
a
# True
not a
# False
True and (True or False)
# True
```

- Puedes usar `if` para hacer comparaciones con diferentes expresiones y definir cuando retornar algo o no. Por ejemplo:

```python
if 3 < 5:
    print("Hi")
    
# Hi
if 5 < 3:
    print("Hi")
    
a = True
b = False
if not b:
    print("Hi")
    
# Hi
if []:
    print("Hi")
    
if [1, 2]:
    print("Hi")
    
# Hi
```

- También existe `else` para cuando la condición en el `if` no sea True. Ejemplo:

```python
if 5 < 3:
    print("Hi")
else:
    print("Bye")
    
# Bye
```

### Loops

- Los `for` loops en Python son simples de leer y escribir, la idea es recorrer un arreglo de valores, creando una variable temporal que será el índice que corresponde como valor: `for temp_value in array:`. Ejemplo:

```python
colors = ["Red", "White", "Green", "Blue"]
for color in colors:
    print(f"The color is: {color}")
    
# The color is: Red
# The color is: White
# The color is: Green
# The color is: Blue
```

- Es importante resaltar, que el valor de `color` sigue existiendo aún fuera del scope del `for loop`, y este tiene el último valor obtenido al recorrer el arreglo.
- Puedes crear un arreglo con `range()` de la siguiente manera:

```python
list(range(3))
# [0, 1, 2]
list(range(3, 7))
# [3, 4, 5, 6]
for number in range(3, 7):
    print(number)
    
# 3
# 4
# 5
# 6
```

- Puedes también obtener el valor y el índice de un arreglo con `enumerate()` respondiendo con una lista de tuplas de la siguiente forma:

```python
colors = ['Red', 'White', 'Green', 'Blue']
list(enumerate(colors))
# [(0, 'Red'), (1, 'White'), (2, 'Green'), (3, 'Blue')]
colors
# ['Red', 'White', 'Green', 'Blue']
for index, color in enumerate(colors):
    print(f"{index} color at: {color}")
    
# 0 color at: Red
# 1 color at: White
# 2 color at: Green
# 3 color at: Blue
```

- Si queremos recorrer un `dict` debemos tener presente que por default un `dict` nos va a devolver las keys. Así que necesitamos pedir explícitamente por las keys y values. Por ejemplo:

```python
hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF",
}
for hex_color in hex_colors:
    print(hex_color)
    
# Red
# Green
# Blue
hex_colors.items()
# dict_items([('Red', '#FF0000'), ('Green', '#008000'), ('Blue', '#0000FF')])
for key, value in hex_colors.items():
    print(f"{key} is value: {value}")
    
# Red is value: #FF0000
# Green is value: #008000
# Blue is value: #0000FF
```

## Practical Applications

### List Comprehensions

- Este es uno de los feature únicos con los que cuenta solo Python, y que incluso por su efectividad, algunos otros lenguajes de programación están comenzando a implementar.
- Veamos un ejemplo de cómo se ve al tomar una lista de nombres y devolvamos una lista de la longitud de cada nombre [aquí](./list_comps.py):

![ejemplo-img-001](./assets/Screenshot%202023-02-21%20at%2013.15.55.png)

- Se puede también incluir condicionales en las `list comprehensions`:

```python
names = ['Alex', 'Elo', 'Tiana', 'Aleisa', 'Jana', 'Ester']
[name for name in names if len(name) % 2 == 0]
# ['Alex', 'Aleisa', 'Jana'] Me está devolviendo solo los nombres que tienen una longitud par
```

- Una forma práctica de crear una lista de un arreglo de nombres dividido por comas es `split()`:

```python
names_string = "Alex,Elo,Tiana,Aleisa,Jana,Ester"
names_string.split(",")
# ['Alex', 'Elo', 'Tiana', 'Aleisa', 'Jana', 'Ester']
```

- También puedes pasar de una lista a un string con `join()`:

```python
names_string = "Alex,Elo,Tiana,Aleisa,Jana,Ester"
names_list = names_string.split(",")
" - ".join(names_list)
# 'Alex - Elo - Tiana - Aleisa - Jana - Ester'
```

- Se pueden realizar operaciones en una `list comprehension`:

```python
num_list = [1, 2, 3]
[num * 2 for num in num_list]
# [2, 4, 6]
", ".join([str(num * 2) for num in num_list])
# '2, 4, 6'
```

### Generator Expresions

- Parece una `list comprehension`, pero a diferencia de estas, se escribe con paréntesis. Al final, este nos devuelve un tipo `generator`. Veamos un ejemplo:

```python
# List comprehension
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
list_comp
# [0, 4, 16, 36, 64]
type(list_comp)
# <class 'list'>

# Generator expression
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
gen_exp
# <generator object <genexpr> at 0x1017854a0>
type(gen_exp)
# <class 'generator'>
```

- Los generadores no ocupan todo el espacio en memoria del resultado obtenido, puedes recorrer el `generator` como lo hemos venido haciendo, pero, hay una diferencia con un arreglo normal, y es que al no tener el espacio en memoria usado, este después de usarse queda exhausto, o sea, ya no es más útil.

```python
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
for item in gen_exp:
    print(item)
    
# 0
# 4
# 16
# 36
# 64
for item in gen_exp:
    print(item)
    
```
