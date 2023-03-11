from collections import defaultdict

# create a dictionary to store words and their meanings
words = defaultdict(set)

# read from file and populate dictionary
# with open('', 'r') as f:
with open('sanskrit_words.txt', encoding='utf-8') as f:

    for line in f:
        parts = line.strip().split()
        word, meaning = parts[0], ' '.join(parts[1:])
        words[meaning].add(word)

# create a list of sets containing words that have the same meaning
word_sets = [set(v) for v in words.values() if len(v) > 2]

# print the sets
for s in word_sets:
    print(s)