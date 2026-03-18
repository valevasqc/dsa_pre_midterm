""" Test de métodos nuevos. """

from ll import Node, LinkedList


# ─── Setup inicial ────────────────────────────────────────────────────────────
ll = LinkedList()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

ll.insert_at_beginning(node_a)
ll.insert_at_beginning(node_b)
ll.insert_at_beginning(node_c)

print("Lista inicial:")
print(ll)
print("Longitud:", len(ll))

print("\nTest traverse:")
ll.traverse()


# ─── insert_at_end ────────────────────────────────────────────────────────────
print("\n--- Test insert_at_end ---")
node_z = Node("Z")
ll.insert_at_end(node_z)
print("Después de insertar 'Z' al final:")
print(ll)

# Edge case: insert_at_end en lista vacía
empty_ll = LinkedList()
empty_ll.insert_at_end(Node("ÚNICO"))
print("\ninsert_at_end en lista vacía:")
print(empty_ll)


# ─── insert_after_node ────────────────────────────────────────────────────────
print("\n--- Test insert_after_node ---")
node_x = Node("X")
ll.insert_after_node(node_x, node_reference="B")
print("Después de insertar 'X' después de 'B':")
print(ll)

# Edge case: referencia inexistente
print("\nBuscando referencia inexistente ('Q'):")
try:
    ll.insert_after_node(Node("Q"), node_reference="Q_FAKE")
except ValueError as e:
    print(f"ValueError capturado correctamente → {e}")


# ─── search ───────────────────────────────────────────────────────────────────
print("\n--- Test search ---")
result = ll.search("X")
print(f"search('X') → {result.data if result else None}")

result = ll.search("NO_EXISTE")
print(f"search('NO_EXISTE') → {result}")


# ─── delete_node ──────────────────────────────────────────────────────────────
print("\n--- Test delete_node ---")
print("Lista antes de eliminar:")
print(ll)

# Eliminar nodo intermedio
ll.delete_node("X")
print("\nDespués de eliminar 'X' (nodo intermedio):")
print(ll)

# Eliminar nodo al inicio (start)
ll.delete_node("C")
print("\nDespués de eliminar 'C' (inicio):")
print(ll)

# Eliminar nodo al final
ll.delete_node("Z")
print("\nDespués de eliminar 'Z' (final):")
print(ll)

# Edge case: dato inexistente
print("\nEliminando dato inexistente ('NO_EXISTE'):")
try:
    ll.delete_node("NO_EXISTE")
except ValueError as e:
    print(f"ValueError capturado correctamente → {e}")

# Edge case: lista vacía
print("\nEliminando de lista vacía:")
try:
    empty_ll2 = LinkedList()
    empty_ll2.delete_node("X")
except ValueError as e:
    print(f"ValueError capturado correctamente → {e}")
