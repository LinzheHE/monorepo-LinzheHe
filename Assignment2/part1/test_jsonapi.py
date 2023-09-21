# use pytest to test the functions defined in jsonapi.property

from jsonapi import *
import pytest

# test the encoder and decoder for complex
def test_encoded():
    test_complex = complex(1, 2)

    encoded_complex = json.dumps(test_complex, cls=MyEncoder)
    decoded_complex = json.loads(encoded_complex, cls=MyDecoder)

    assert decoded_complex == test_complex


# test the encoder and decoder for range
def test_decoded():
    test_range = range(1, 10, 3)

    encoded_range = json.dumps(test_range, cls=MyEncoder)
    decoded_range = json.loads(encoded_range, cls=MyDecoder)
    
    assert decoded_range == test_range

