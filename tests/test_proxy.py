from structural.proxy import Proxy


def test_producer_is_available():
    """It returns correct value when producer is available"""
    proxy = Proxy()

    response = proxy.produce()

    assert response == "Resource intensive produce from producer"


def test_producer_is_occupied():
    """It does not allow producer to be instantiated"""
    proxy = Proxy()

    proxy.occupied = "Yes"
    response = proxy.produce()

    assert response == "Producer is not available"
