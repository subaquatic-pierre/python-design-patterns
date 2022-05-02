class Borg:
    _data = {}


class Singleton(Borg):
    def __init__(self, **kwargs) -> None:
        Borg._data.update(kwargs)

        self.__dict__ = Borg._data

    def __str__(self) -> str:
        return str(self.__dict__)


padi = Singleton(PADI="Profesional Association of Diving Instrcutrors")

print(padi)

tdi = Singleton(TDI="Technical Diving Instrcutors")

print(tdi)

new_padi = Singleton(PADI="Put Another Dollar In")

print(new_padi)
