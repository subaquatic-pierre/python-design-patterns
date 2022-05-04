from abc import abstractmethod


class Component:
    def __init__(self, *args, **kwargs) -> None:
        self.name = args[0]

    @abstractmethod
    def component_function(self):
        pass


class Composite(Component):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._children = []

    def append_child(self, child):
        self._children.append(child)

    def remove_child(self, child):
        self._children.remove(child)

    def component_function(self):
        print(self.name)

        for child in self._children:
            child.component_function()


class Child(Component):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def component_function(self):
        print(self.name)
