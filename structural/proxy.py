from time import sleep


class Producer:
    """Resourec intensive producer class"""

    def produce(self):
        return "Resource intensive produce from producer"

    def meet(self):
        """Producer meets guest"""
        return "Producer is available to meet."


class Proxy:
    def __init__(self) -> None:
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Main produce method"""

        if self.occupied == "No":
            self.producer = Producer()

            print(self.producer.meet())
            return self.producer.produce()

        else:
            return "Producer is not available"
