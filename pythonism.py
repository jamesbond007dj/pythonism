from functools import wraps

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def __str__(self):
        return str(list(iter(self)))

    def __len__(self):
        return len(list(iter(self)))

    def __iter__(self):
        def generator():
            current = self.head

            while current:
                yield current.value
                current = current.next

        return generator()

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node


def append(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs) + 1
        return value

    return wrapper


@append
def multiply_by_two(value):
    return value + value