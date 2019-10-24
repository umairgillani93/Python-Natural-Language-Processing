corpus = 'This is the test corpus. In order to play around with NLP techniques you have to have a precise corpus with you'

# print(corpus)

word_counts = {}

for word in corpus.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts["a"] / len(corpus.split()))

term_freq = {}

for word in corpus.split():
    term_freq[word] = word_counts[word] / len(corpus.split())

print(word_counts)
print('\n')
print(term_freq)
print('=' * 20)

# Reports back the term frequencies of the words in given Corpus!
