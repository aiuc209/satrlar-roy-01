import pytest

def reverse_words_in_sentences(sentences):
    return [' '.join(word[::-1] for word in sentence.split()) for sentence in sentences]

def test_reverse_words_in_sentences():
    sentences = ["Hello world", "Python is fun"]
    expected_output = ["olleH dlrow", "nohtyP si nuf"]
    assert reverse_words_in_sentences(sentences) == expected_output

def test_empty_list():
    sentences = []
    expected_output = []
    assert reverse_words_in_sentences(sentences) == expected_output

def test_single_word_sentence():
    sentences = ["Hello"]
    expected_output = ["olleH"]
    assert reverse_words_in_sentences(sentences) == expected_output

def test_multiple_word_sentence():
    sentences = ["Hello world this is python"]
    expected_output = ["olleH dlrow siht si nohtyp"]
    assert reverse_words_in_sentences(sentences) == expected_output
