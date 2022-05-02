from copy import deepcopy


class Prototype:
    """Main prototype class"""

    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        """Register object with prototype"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregsiter an object"""
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj


class ScubaRegulator:
    def __init__(self, brand, first_stage, second_stage) -> None:
        self.brand = brand
        self.first_stage = first_stage
        self.second_stage = second_stage

    def __str__(self) -> str:
        return f"Regulator Brand: {self.brand} | First Stage: {self.first_stage}| Second Stage: {self.second_stage}"


prototype = Prototype()
scubapro_reg = ScubaRegulator("Scuba Pro", "MK25", "A700")
prototype.register_object("scubapro", scubapro_reg)

scubapro_copy = prototype.clone("scubapro", first_stage="MK17")

print(scubapro_reg)
print(scubapro_copy)
