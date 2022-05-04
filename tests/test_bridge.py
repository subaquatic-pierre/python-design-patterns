from structural.bridge import Circle, DrawAPIOne, DrawAPITwo


def test_invokes_api_one():
    circle = Circle(1, 2, 3, DrawAPIOne())
    response = circle.draw()

    assert response == "Draw API 1, X: 1, Y: 2, Radius: 3"


def test_invokes_api_two():
    circle = Circle(1, 2, 3, DrawAPITwo())
    response = circle.draw()

    assert response == "Draw API 2, X: 1, Y: 2, Radius: 3"


def test_scales():
    circle = Circle(1, 2, 3, DrawAPIOne())

    circle.scale(2)

    response = circle.draw()

    assert response == "Draw API 1, X: 1, Y: 2, Radius: 6"
