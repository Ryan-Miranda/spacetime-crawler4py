from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Tokenizer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def word_tokenizer_count(self, lines):
        word_tokens = word_tokenize(lines)
        word_count = dict()
        for word in word_tokens:
            word = word.lower()
            if word in self.stop_words or len(word) <= 2:
                continue

            if word not in word_count:
                word_count[word] = 0

            word_count[word] += 1

        return word_count
