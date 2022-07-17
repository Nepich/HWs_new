from abc import ABCMeta, abstractmethod, ABC


class Node:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_other_node(self):
        pass


class StrNode(Node):
    def __init__(self, some_text: str, other=None):
        self.some_text = some_text
        self.other = other

    def get_other_node(self) -> Node:
        if self.other:
            return self.other


class IntNode(Node):
    def __init__(self, some_int: int, other):
        self.some_int = some_int
        self.other = other

    def get_other_node(self) -> Node:
        if self.other:
            return self.other
