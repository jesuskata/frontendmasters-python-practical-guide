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