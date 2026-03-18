''' Custom Linked List implementation. '''


class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'(DATA: {self.data} | NEXT: {self.next})' # TODO: En el futuro arreglar repr para mostrar solo la data, error cuando next es None 


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        nodes = ['START']
        for node in self:
            nodes.append(node.data)
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

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
        pass

    def insert_after_node(self, element: Node, node_reference: any):
        pass
    
    def delete_node(self, element_data: any):
        # Deletes the first node with matching data
        pass

    def search(self, element_data: any):
        # Returns the first node with matching data
        pass
