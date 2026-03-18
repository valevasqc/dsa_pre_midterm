from ll import Node, LinkedList

node_a = Node("Maldita costumbre", "Morat", "Balas Perdidas")
node_b = Node("Cómo te atreves", "Morat", "Sobre el amor")

ll = LinkedList()
ll.insert_at_beginning(node_a)
ll.insert_at_beginning(node_b)
print(ll)