import heapq
import re

import nltk

from text import text

nltk.download("stopwords", "model")
nltk.download("punkt", "model")
nltk.data.path = ["model"]

lines = [line for line in text.split('\n') if line.strip() != '']

formatted_text = re.sub(r'\s+', ' ', text)
formatted_text = re.sub('[^a-zA-ZÄÖÜäöüß]', ' ', text)

stopwords = nltk.corpus.stopwords.words('german')
sentences = nltk.sent_tokenize(" ".join(lines))

word_frequencies = {}
for word in nltk.word_tokenize(formatted_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

sentence_scores = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_frequencies.keys():
            if sentence not in sentence_scores.keys():
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]

summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary_sentences.sort(key=lambda x: sentences.index(x))

summary = ' '.join(summary_sentences)

print(summary)
