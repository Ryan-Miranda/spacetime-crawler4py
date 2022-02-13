import csv
import re


def clear_text(text):
    tmp = re.sub(r'[^\w\s]', '', text)
    return tmp.lower().replace('\n', ' ')


def calculate_checksum(data):
    chk_sum = sum([int(ord(data[i])) for i in range(len(data))])
    return chk_sum


def exact_similarity_checksum_score(data1, data2):
    return calculate_checksum(clear_text(data1)) == calculate_checksum(clear_text(data2))


def xor(x, y):
    res = []
    for i in range(0, len(y)):
        if x[i] == y[i]:
            res.append('0')
        else:
            res.append('1')
    return ''.join(res)


# https://www.geeksforgeeks.org/modulo-2-binary-division/
def calc_remainder(data, divisor):
    pick = len(divisor)
    tmp = data[0: pick]
    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + data[pick]
        else:
            tmp = xor('0' * pick, tmp) + data[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    remainder = tmp
    return remainder


def exact_similarity_crc_score(data1, data2):
    divisor = '1010'
    data1 = str(hash(clear_text(data1)))
    data2 = str(hash(clear_text(data2)))
    data1 = ''.join(format(ord(x), 'b') for x in data1)
    data2 = ''.join(format(ord(x), 'b') for x in data2)
    if len(data1) > len(data2):
        data2 = '0' * (len(data1) - len(data2)) + data2
    elif len(data1) < len(data2):
        data1 = '0' * (len(data2) - len(data1)) + data1

    data1 = data1 + '0' * (len(divisor) - 1)
    remainder1 = calc_remainder(data1, divisor)
    data2 = data2 + '0' * (len(divisor) - 1)
    remainder2 = calc_remainder(data2, divisor)
    if remainder1 == remainder2:
        return True
    return False


def get_dict(d):
    words = dict()
    data = d.split('|')
    for d in data[:len(data) - 1]:
        tmp = d[::-1]
        cnt, word = int(tmp[:tmp.index(',')][::-1]), tmp[tmp.index(',') + 1:][::-1]
        if word not in words:
            words[word] = 0
        words[word] += cnt
    return words


def calculate_hash(data):
    hash_val = dict()
    vector = [0 for i in range(66)]
    for d in data:
        tmpHash = str(abs(hash(d)) % (10 ** 11))
        hash_val[d] = ''.join(format(ord(x), 'b') for x in str(tmpHash))
        if len(hash_val[d]) < 66:
            hash_val[d] = '0' * (66 - len(hash_val[d])) + hash_val[d]

        for j in range(66):
            if hash_val[d][j] == '0':
                vector[j] += (-1 * int(data[d]))
            else:
                vector[j] += int(data[d])

    return hash_val, vector


# {'statistics': 12, 'department': 8, '2021': 8, 'data': 7, 'science': 7...
def calc_simhash(data):
    hash_val, vector = calculate_hash(data)
    finger_print = []
    for v in vector:
        if v > 0:
            finger_print.append(1)
        else:
            finger_print.append(0)

    return finger_print


def simhash_similarity_score(finger_print1, finger_print2):
    cnt = 0
    for i in range(len(finger_print1)):
        if finger_print1[i] == finger_print2[i]:
            cnt += 1
    return float(cnt) / len(finger_print1)


def fingerprinting_similarity_score(finger_print1, finger_print2):
    cnt = 0
    for i in range(len(finger_print1)):
        if finger_print1[i] == finger_print2[i]:
            cnt += 1
    return float(cnt) / (2 * len(finger_print1))


# exact_similarity_checksum_score(d0, d1)
# exact_similarity_crc_score(d0, d1)
# calc_simhash(data_weights)
# simhash_similarity_score(finger_print1, finger_print2)
# fingerprinting_similarity_score(finger_print1, finger_print2)
