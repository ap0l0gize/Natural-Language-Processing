import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
import urllib.request
from matplotlib import pyplot as plt
from wordcloud import WordCloud
nltk.download('punkt')

#read and decode text
with open("germanText.txt", "r", encoding="utf-8") as f:
    text = f.read()

#tokenize text by words
words = word_tokenize(text)

#check the number of words
print(f"Number of words in the text (with punctuation): {len(words)}")

#create an empty list to store words
words_no_punc = []

#iterate through the words list to remove punctuations
for word in words:
    if word.isalpha():
        words_no_punc.append(word.lower())

#print number of words without punctuation
print(f"Number of words without punctuation: {len(words_no_punc)}")

f_words_no_punc = FreqDist(words_no_punc)

print(f_words_no_punc.most_common(10))

frequencies = sorted(f_words_no_punc.values(), reverse=True)
ranks = range(1, len(frequencies) + 1)

plt.figure(figsize=(8,5))
plt.loglog(ranks, frequencies)
plt.xlabel("Rank (r)")
plt.ylabel("Frequency (f)")
plt.title("Zipf's Law - log-log plot")
plt.grid(True)
plt.show()
