import re
import heapq
from collections import defaultdict
from typing import List

import nltk
nltk.download("punkt")
nltk.download("stopwords")
from nltk.corpus import stopwords

# One-time NLTK setup
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")
    nltk.download("punkt")


def summarize(text: str, max_sentences: int = 3) -> str:
    # Clean and split text
    text = re.sub(r'\s+', ' ', text)
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text.lower())

    # Filter stopwords
    stop_words = set(stopwords.words("english"))
    word_frequencies = defaultdict(int)

    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] += 1

    if not word_frequencies:
        return "No meaningful content to summarize."

    # Score sentences
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Get top N sentences
    summary_sentences: List[str] = heapq.nlargest(max_sentences, sentence_scores, key=sentence_scores.get)
    return " ".join(summary_sentences)
