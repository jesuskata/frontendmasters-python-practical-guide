names = ["Alex", "Elo", "Tiana", "Aleisa", "Jana", "Ester"]

my_list = [] # An empty list

for name in names:
    my_list.append(len(name))

print("Before: ", my_list)

# [] comenzamos con una lista
# [for name in names] recorremos dentro de la lista el arreglo
# [len(name) for name in names] al inicio del arreglo escribimos lo que esperamos de ese for loop
print("After", [len(name) for name in names])
