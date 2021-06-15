from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pandas
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["adult", "bird","boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    for i in range(10):
        word = get_noun(1)
        assert word in singular_nouns
    
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for i in range(10):
        word = get_noun(0)
        assert word in plural_nouns


def test_get_verbs():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for i in range(10):
        word = get_verb(1, 'past')
        assert word in past_verbs

    present_singular_verbs = ["drinks", "eats", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for i in range(10):
        word = get_verb(1, 'present')
        assert word in present_singular_verbs

    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for i in range(10):
        word = get_verb(0, "present")
        assert word in present_plural_verbs 
    
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",  "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for i in range(10):
        word = get_verb(1, 'future')
        assert word in future_verbs

def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for i in range(31):
        word = get_preposition()
        assert word in preposition

def test_get_prepositional_phrase():
    for i in range(10):
        word = str.split(get_prepositional_phrase(1))
        assert len(word) == 3
    
    for i in range(10):
        word = str.split(get_prepositional_phrase(0))
        assert len(word) == 3
    
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])







