from jsonapi import *

# test the encoder and decoder for complex
test_complex = complex(1, 2)
print("original complex:", test_complex)

encoded_complex = json.dumps(test_complex, cls=MyEncoder)
print("encoded complex:", encoded_complex)

decoded_complex = json.loads(encoded_complex, cls=MyDecoder)
print("decoded complex:", decoded_complex)


# test the encoder and decoder for range
test_range = range(1, 10, 3)
print("original range:", test_range)

encoded_range = json.dumps(test_range, cls=MyEncoder)
print("encoded range:", encoded_range)

decoded_range = json.loads(encoded_range, cls=MyDecoder)
print("decoded range:", decoded_range)

