'''
Invertir una lista usando un stack.
'''

from stack import Stack


original_list = ['3', '14', '33', '42', '55']
aux_stack = Stack(len(original_list))

# Stack inicial y lista
print(f'Lista original: {original_list}')
print(aux_stack)

# Poblar el stack auxiliar
for num in original_list:
    aux_stack.push(num)

# Stack poblado
print(aux_stack)

# Crear nueva lista
new_list = []

# Vaciar stack en nueva lista
while aux_stack.peek() != 'Stack Underflow':
    num = aux_stack.pop()
    new_list.append(num)

# Stack vacio y nueva lista
print(aux_stack)
print(f'Nueva lista: {new_list}')
