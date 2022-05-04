class EnglishSpeaker:
    def __init__(self) -> None:
        self.name = "English"

    def speak_english(self):
        return "Speak English"


class GermanSpeaker:
    def __init__(self) -> None:
        self.name = "German"

    def speak_german(self):
        return "Speak German"


class Adapter:
    def __init__(self, object, **adapted_method) -> None:
        self._object = object

        self._object.__dict__.update(adapted_method)

    def __getattr__(self, _name: str):
        return getattr(self._object, _name)
