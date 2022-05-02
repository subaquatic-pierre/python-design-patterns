from creational.builder import Director, NissanPatrolBuilder


def test_create_car():
    """It creates a new car successfully with correct attributes"""
    builder = NissanPatrolBuilder()
    director = Director(builder)

    director.construct_car()
    car = director.get_car()

    assert car.model == "Nissan Patrol"
    assert car.tires == "Yokohama Tires"
    assert car.engine == "Nissan V8 Turbo"
    assert car.stereo == "Rokford Fosgate SubWoofer"
