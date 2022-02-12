"""
http://languagelog.ldc.upenn.edu/myl/Shannon1950.pdf
"""
import re
from math import log2


def clear_text(text):
    return re.sub(r'[^\w\s]', '', text)


def get_ngram_count(data, ngram):
    n_gram_count = dict()
    ln = 0
    while ln < len(data):
        tmp_n_gram_str = data[ln:ln + ngram]
        ln += ngram
        if tmp_n_gram_str not in n_gram_count:
            n_gram_count[tmp_n_gram_str] = 0
        n_gram_count[tmp_n_gram_str] += 1
    return n_gram_count


def get_ngram_probabilities(n_gram_count):
    total = sum(n_gram_count.values())
    ngram_prob = dict()
    for k, v in n_gram_count.items():
        ngram_prob[k] = v / float(total)

    return ngram_prob


def calc_entropy(ngram_prob):
    tmp_entropy = [(p * log2(p)) for p in ngram_prob.values()]
    return -sum(tmp_entropy)


def ngram_entropy(data, ngram=8):  # Default is 1-gram
    data = clear_text(data).lower().replace('\n', ' ')
    n_gram_count = get_ngram_count(data, ngram)
    n_gram_prob = get_ngram_probabilities(n_gram_count)
    H = calc_entropy(n_gram_prob)
    return H


def fingerprinting_similarity_score():
    pass

#
# if __name__ == '__main__':
#     f_lorem_ipsum = '../tmp/test/loremipsum'
#     eng_small = '../tmp/test/english0'
#     eng_1 = '../tmp/test/english1'
#     for i in range(1, 11):
#         print('n-gram N : ', i)
#         with open(eng_1, 'r') as f:
#             lines = f.readlines()
#             ngram_entropy(''.join(lines), i)
#
#         with open(eng_small, 'r') as f:
#             lines = f.readlines()
#             ngram_entropy(''.join(lines), i)
#
#         with open(f_lorem_ipsum, 'r') as f:
#             lines = f.readlines()
#             ngram_entropy(''.join(lines), i)
#         print('====================')
