import nltk

nltk.download('words')

tokens = nltk.word_tokenize('Hey! how are you?')
print('Tokens: ', tokens)

parts_of_speech = nltk.pos_tag(tokens)

print(parts_of_speech[:])

# Named Entity Recognition

entities = nltk.chunk.ne_chunk(parts_of_speech)
print(entities)
