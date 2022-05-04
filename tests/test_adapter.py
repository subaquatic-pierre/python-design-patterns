from structural.adapter import Adapter, EnglishSpeaker, GermanSpeaker


def test_english_speaker():
    english_speaker = EnglishSpeaker()

    adapted = Adapter(english_speaker, speak=english_speaker.speak_english)

    # Call adapter method
    response = adapted.speak()

    assert response == "Speak English"


def test_german_speaker():
    german_speaker = GermanSpeaker()

    adapted = Adapter(german_speaker, speak=german_speaker.speak_german)

    # Call adapter method
    response = adapted.speak()

    assert response == "Speak German"
