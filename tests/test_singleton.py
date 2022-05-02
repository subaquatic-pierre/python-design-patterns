from creational.singleton import Singleton


def test_dict_is_equal():
    """It only creates one singleton instance, with the same dict struct"""

    padi = Singleton(PADI="Profesional Association of Diving Instrcutrors")
    tdi = Singleton(TDI="Technical Diving Instrcutors")

    assert padi._data == tdi._data


def test_updates_dict():
    """It updates the Singleton with new value"""
    padi = Singleton(PADI="Profesional Association of Diving Instrcutrors")
    new_padi = Singleton(PADI="Put Another Dollar In")

    assert padi._data.get("PADI") == "Put Another Dollar In"
