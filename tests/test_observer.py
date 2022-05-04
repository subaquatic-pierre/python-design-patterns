from behavioral.observer import Observer, Reactor
from unittest.mock import patch


@patch("builtins.print")
def test_notifies_all_observers(mock_print):
    reactor = Reactor("Abu Dhabi")

    worker1 = Observer("Worker 1")
    worker2 = Observer("Worker 2")

    reactor.attach(worker1)
    reactor.attach(worker2)

    reactor.temp = 30

    assert mock_print.call_count == 2


def test_attaches_new_observer():
    reactor = Reactor("Abu Dhabi")

    assert len(reactor._observers) == 0

    worker1 = Observer("Worker 1")
    worker2 = Observer("Worker 2")

    reactor.attach(worker1)
    reactor.attach(worker2)

    assert len(reactor._observers) == 2


def test_detaches_observer():
    reactor = Reactor("Abu Dhabi")

    assert len(reactor._observers) == 0

    worker1 = Observer("Worker 1")
    worker2 = Observer("Worker 2")

    reactor.attach(worker1)
    reactor.attach(worker2)

    assert len(reactor._observers) == 2

    reactor.detach(worker1)

    assert len(reactor._observers) == 1
