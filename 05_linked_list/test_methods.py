'''
Test de métodos nuevos.
'''


from ll import Node, LinkedList


# Crear nuevo LL
ll = LinkedList()

# Instanciar nodo A
node_a = Node('A')

# Insertar elementos al inicio
node_b = Node('B')
node_c = Node('C')

ll.insert_at_beginning(node_a)
ll.insert_at_beginning(node_b)
ll.insert_at_beginning(node_c)
print(ll)

print(len(ll))

# Test Traverse()
print('\nTest traverse:')
ll.traverse()



