class Subject:
    def __init__(self, *args, **kwargs) -> None:
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Reactor(Subject):
    def __init__(self, name="", *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, val):
        self._temp = val

        # notify observers
        self.notify()


class Observer:
    def __init__(self, name) -> None:
        self.name = name

    def update(self, subject):
        print(f"{self.name} has been updated with new temp: {subject.temp}")
