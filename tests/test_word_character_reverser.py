import pytest
from src.word_character_reverser import reverse_words_and_characters

def test_basic_reverse():
    """Test basic word and character reversal"""
    assert reverse_words_and_characters("Hello World") == "dlroW olleH"
    assert reverse_words_and_characters("Python is awesome") == "emosewa si nohtyP"

def test_single_word():
    """Test single word input"""
    assert reverse_words_and_characters("Python") == "nohtyP"

def test_multiple_words():
    """Test multiple words"""
    assert reverse_words_and_characters("one two three") == "eerht owt enO"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words_and_characters("") == ""

def test_string_with_spaces():
    """Test string with multiple spaces"""
    assert reverse_words_and_characters("  Hello   World  ") == "dlroW olleH"

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        reverse_words_and_characters(123)
    with pytest.raises(TypeError):
        reverse_words_and_characters(None)