from markov import tokenize, generate
import pytest

def test_tokenize():
    assert tokenize("Hello, world!") == ["Hello", ",", "world", "!"]

def test_generate_returns_text():
    result = generate("a b c a b c a b c", order=1, length=10, seed=4)
    assert isinstance(result, str) and len(result) > 0

def test_invalid_order():
    with pytest.raises(ValueError):
        generate("a b c d e", order=3, length=5)
