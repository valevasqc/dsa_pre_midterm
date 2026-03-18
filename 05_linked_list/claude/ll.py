""" Custom Linked List implementation. """


class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        # TODO: En el futuro arreglar repr para mostrar solo la data,
        # error cuando next es None
        return f"(DATA: {self.data} | NEXT: {self.next})"


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        nodes = ["START"]
        for node in self:
            nodes.append(str(node.data))
        nodes.append("NIL")
        return "\n" + " --> ".join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self):
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node):
        element.next = self.start
        self.start = element

    def insert_at_end(self, element: Node):
        """Inserts a node at the end of the list."""
        if self.start is None:
            self.start = element
            return
        current = self.start
        while current.next is not None:
            current = current.next
        current.next = element

    def insert_after_node(self, element: Node, node_reference: any):
        """Inserts a node immediately after the first node whose data
        matches node_reference. Raises ValueError if not found."""
        for current in self:
            if current.data == node_reference:
                element.next = current.next
                current.next = element
                return
        raise ValueError(
            f"Node with data '{node_reference}' not found in the list."
        )

    def delete_node(self, element_data: any):
        """Deletes the first node with matching data.
        Raises ValueError if not found."""
        if self.start is None:
            raise ValueError("Cannot delete from an empty list.")

        if self.start.data == element_data:
            self.start = self.start.next
            return

        previous = self.start
        for current in self:
            if current.data == element_data:
                previous.next = current.next
                return
            previous = current

        raise ValueError(
            f"Node with data '{element_data}' not found in the list."
        )

    def search(self, element_data: any):
        """Returns the first node with matching data, or None if not found."""
        for node in self:
            if node.data == element_data:
                return node
        return None
