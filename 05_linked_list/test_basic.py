'''
Test for Linked List.
'''


from ll import Node, LinkedList


# Instancia Node
node_a = Node('A')
print(node_a)

# Instancia LL
ll = LinkedList()
print(ll)

# Asignar Nodo A como start de LL (manualmente)
ll.start = node_a
print(ll)

# Agregar Nodo B como segundo elemento (manualmente)
node_b = Node('B')
ll.start.next = node_b
print(ll)
