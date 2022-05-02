from creational.prototype import Prototype, ScubaRegulator


def test_creates_copy():
    """It creates a new copy of the object"""

    prototype = Prototype()
    scubapro_reg = ScubaRegulator("Scuba Pro", "MK25", "A700")
    prototype.register_object("scubapro", scubapro_reg)

    scubapro_copy = prototype.clone("scubapro")

    assert scubapro_reg.brand == scubapro_copy.brand
    assert scubapro_reg.first_stage == scubapro_copy.first_stage
    assert scubapro_reg.second_stage == scubapro_copy.second_stage


def test_updates_attrs():
    """It updates attrs with new attrs on copy"""
    prototype = Prototype()
    scubapro_reg = ScubaRegulator("Scuba Pro", "MK25", "A700")
    prototype.register_object("scubapro", scubapro_reg)

    scubapro_copy = prototype.clone("scubapro", first_stage="MK17")

    assert scubapro_reg.first_stage != scubapro_copy.first_stage
    assert scubapro_copy.first_stage == "MK17"


def test_unregister_object():
    """It deletes obj on Prototype.unregister call"""
    prototype = Prototype()
    scubapro_reg = ScubaRegulator("Scuba Pro", "MK25", "A700")
    prototype.register_object("scubapro", scubapro_reg)

    assert "scubapro" in prototype._objects

    prototype.unregister_object("scubapro")

    assert "scubapro" not in prototype._objects
