import pytest
from src.ngram_model import NgramModel

def test_fit_and_generate(): # give n=number (any ) as argument for creating any ngram model
    model = NgramModel()
    text = "I am a test sentence. This is another test sentence."
    model.fit(text)
    model.generate()  # give min = number and max = number  to genereate minimum words even after end token  default max=50
    generated_text = model.generate()
    assert isinstance(generated_text, str)
    assert len(generated_text.split()) > 0

def test_empty_text():
    model = NgramModel()
    text = ""
    model.fit(text)
    generated_text = model.generate()
    assert generated_text == ""

def test_short_text():
    model = NgramModel()
    text = "I am."
    model.fit(text)
    generated_text = model.generate()
    assert isinstance(generated_text, str)
