import tiktoken


# first encoding 

Encoding = tiktoken.encoding_for_model('gpt-4o')

text = 'Hi Am Muhammad Atif khan'

enc = Encoding.encode(text)

print('Encoded Tokens ' , enc)

# output is : Encoded Tokens  [12194, 4820, 67641, 3604, 366, 5752, 270]


# Now use Decoder

Decoded = Encoding.decode( [12194, 4820, 67641, 3604, 366, 5752, 270])

print(Decoded)