from abc import abstractmethod


class Builder:
    """Abstract Builder"""

    def __init__(self) -> None:
        self.car = None

    def build_car(self):
        self.car = Car()

    @abstractmethod
    def add_model(self):
        pass

    @abstractmethod
    def add_tires(self):
        pass

    @abstractmethod
    def add_engine(self):
        pass

    @abstractmethod
    def add_stereo(self):
        pass


class Director:
    """Director Class"""

    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def construct_car(self):
        self._builder.build_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()
        self._builder.add_stereo()

    def get_car(self):
        return self._builder.car


class NissanPatrolBuilder(Builder):
    """Concrete Builder"""

    def add_model(self):
        self.car.model = "Nissan Patrol"

    def add_tires(self):
        self.car.tires = "Yokohama Tires"

    def add_engine(self):
        self.car.engine = "Nissan V8 Turbo"

    def add_stereo(self):
        self.car.stereo = "Rokford Fosgate SubWoofer"


class Car:
    def __init__(self) -> None:
        self.model = None
        self.tires = None
        self.engine = None
        self.stereo = None

    def __str__(self) -> str:
        return f"{self.model} - Engine: {self.engine} - Tires: {self.tires} - Stereo: {self.stereo}"


builder = NissanPatrolBuilder()
director = Director(builder)

director.construct_car()
car = director.get_car()

print(car)
