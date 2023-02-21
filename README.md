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