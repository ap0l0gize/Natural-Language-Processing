import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from matplotlib import pyplot as plt

nltk.download('punkt')

nltk.download('punkt_tab')

#read and decode text
with open("germanText.txt", "r", encoding="utf-8") as f:
    text = f.read()

#tokenize text by words
words = word_tokenize(text, language='german')

#check the number of words
print(f"Number of words in the text (with punctuation): {len(words)}")

#create an empty list to store words
words_no_punc = []

#iterate through the words list to remove punctuations
for word in words:
    if word.isalpha():
        words_no_punc.append(word.lower())


total_words = len(words_no_punc)

#print number of words without punctuation
print(f"Number of words without punctuation: {total_words}")

f_words_no_punc = FreqDist(words_no_punc)

frequencies = sorted(f_words_no_punc.values(), reverse=True)
ranks = range(1, len(frequencies) + 1)

# How many words do you have to know in order to learn 90% of language?

ninty_percent_threshold = 0.9
cumulative_coverage = 0
num_of_words = 0

for frequency in frequencies:
    cumulative_coverage += (frequency / total_words)
    num_of_words += 1
    if cumulative_coverage >= ninty_percent_threshold:
        break

print(f"Number of words needed to learn 90% of language: {num_of_words}")

# Words needed to learn 90% of German.
most_common_words = f_words_no_punc.most_common(num_of_words)
# print(most_common_words)


plt.figure(figsize=(8,5))
plt.loglog(ranks, frequencies)
plt.xlabel("Rank (r)")
plt.ylabel("Frequency (f)")
plt.title("Zipf's Law - log-log plot")
plt.grid(True)
plt.show()
