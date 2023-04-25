class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Stack:

    def __init__(self, limit=None, top_item=None):
        self.top = top_item
        self.size = 0
        self.limit = limit
        if self.top is not None and limit > 1:
            self.size += 1

    def peek(self):
        return self.top

    def push_n(self, node):
        if self.has_space():
            print("Stack Full")
            return
        node.set_next_node(self.top)
        self.top = node
        self.size += 1

    def push_v(self, value):
        if self.has_space():
            print("Stack Full")
            return
        n = Node(value)
        n.set_next_node(self.top)
        self.top = n
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.limit

    def pop(self):
        if self.size == 0:
            print("Stack empty")
            return
        pop = self.top
        self.top = self.top.get_next_node()
        pop.set_next_node(None)
        self.size -= 1
        return pop





