import pytest
from src.keyboard import Keyboard, Language


@pytest.fixture
def lang():
    return Language()


def test_language_init(lang):
    assert lang.language == "EN"


def test__str__language(lang):
    assert str(lang) == "EN"


def test_change_lang(lang):
    assert str(lang.change_lang()) == "RU"


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(kb):
    assert str(kb) == "Dark Project KD87A"
    assert kb.language == "EN"


def test_keyboard_change_lang(kb):
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"
    kb.change_lang().change_lang()
    assert kb.language == "EN"


def test_set_language(kb):
    with pytest.raises(AttributeError):
        kb.language = 'CH'
