from abc import abstractmethod


class House:
    def accept(self, visitor):
        return visitor.visit(self)

    def hvac_work(self, specialist):
        return f"House worked on by {specialist}"

    def electrical_work(self, specialist):
        return f"House worked on by {specialist}"


class Visitor:
    @abstractmethod
    def visit(self, house):
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class Electrician(Visitor):
    def visit(self, house):
        return house.electrical_work(self)


class Hvac(Visitor):
    def visit(self, house):
        return house.hvac_work(self)
