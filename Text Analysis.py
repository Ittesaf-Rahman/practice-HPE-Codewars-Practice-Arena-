from collections import Counter

text = """Text analysis is the process of extracting meaningful information 
from text data. It involves techniques such as word frequency analysis."""

words = text.lower().split()
word_count = Counter(words)

print("Total words:", len(words))
print("Unique words:", len(set(words)))
print("Most common words:", word_count.most_common(3))
