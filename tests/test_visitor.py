from behavioral.visitor import Electrician, Hvac, House


def test_electrical_work():
    home = House()
    e = Electrician()

    response = home.accept(e)

    assert response == "House worked on by Electrician"


def test_hvac_work():
    home = House()
    e = Hvac()

    response = home.accept(e)

    assert response == "House worked on by Hvac"
