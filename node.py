class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str("<{}: {}>".format(type(self), self.value))

class TwoWayNode(Node):
    def __init__(self, previous, value):
        if type(previous) is not Node:
            raise TypeError("previous should be Node")

        super(value)
        self.previous = previous