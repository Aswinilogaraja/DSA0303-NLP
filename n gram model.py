import random
from collections import defaultdict
import nltk

# Sample corpus for training the bigram model
corpus = "This is a sample corpus. You can replace it with your own text data. Tokenization is necessary."

# Tokenize the corpus into words
tokens = nltk.word_tokenize(corpus)

# Create a defaultdict to store bigram frequencies
bigram_freq = defaultdict(lambda: defaultdict(int))

# Generate bigrams and count their frequencies
for i in range(len(tokens) - 1):
    bigram_freq[tokens[i]][tokens[i + 1]] += 1

# Generate text using the bigram model
def generate_text_bigram(bigram_freq, length=10):
    # Start the generated text with a random word from the corpus
    current_word = random.choice(list(bigram_freq.keys()))
    generated_text = [current_word]

    # Generate text based on the bigram model
    for _ in range(length - 1):
        next_word = random.choice(list(bigram_freq[current_word].keys()))
        generated_text.append(next_word)
        current_word = next_word

    return ' '.join(generated_text)

# Generate and print a sample text using the bigram model
generated_text = generate_text_bigram(bigram_freq, length=20)
print("Generated Text (Bigram Model):", generated_text)
