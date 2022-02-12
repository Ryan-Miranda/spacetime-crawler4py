import csv
import os


class GenerateResult:
    def __init__(self):
        self.top50Word = dict()
        self.subdomain_urls = dict()

    def get_unique_pages_list(self):
        cnt = 0
        with open('../tmp/unique_file_urls.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                cnt += 1
        print("Count of Unique URLS visted : ", (cnt - 1))

    def longest_page_interms_of_word_count(self):
        path = '../tmp/pg_index_example.txt'
        if not os.path.isfile(path):
            print('ERROR :: Something went wrong file does not exist.')
            return
        max_size_page, max_size_url = 0, ''
        top50Word = dict()
        with open(path, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter='\t')
            skip = True
            for row in reader:
                if skip:
                    skip = False
                    continue
                if int(row[0]) > max_size_page:
                    max_size_page = int(row[0])
                    max_size_url = row[2]
                self.get_top50Words(row[3])
                self.get_subdomains(row[2])

        print(f'Max sized page: {max_size_page} from url: {max_size_url}')

    def get_top50Words(self, d):
        data = d.split('|')
        for d in data[:len(data) - 1]:
            tmp = d[::-1]
            cnt, word = int(tmp[:tmp.index(',')][::-1]), tmp[tmp.index(',') + 1:][::-1]
            if word not in self.top50Word:
                self.top50Word[word] = cnt
                continue
            self.top50Word[word] += cnt
        return

    def display_top50_words(self):
        top50Word_sorted = sorted(self.top50Word.items(), key=lambda d: d[1], reverse=True)[:50]
        print('Top overall 50 words: ')
        for a, b in top50Word_sorted:
            print(f'{a}\t{b}')

    def get_subdomains(self, subdomain):
        t = 'ics.uci.edu'
        if subdomain.__contains__(t):
            key = subdomain[subdomain.index('://') + 3:subdomain.index(t) + len(t)]
            if key not in self.subdomain_urls:
                self.subdomain_urls[key] = 0
            self.subdomain_urls[key] += 1

    def display_subdomain(self):
        print('Sub Domains: ')
        for k in self.subdomain_urls:
            print(f'{k}, {self.subdomain_urls[k]}')

    def get_longest_page(self):
        pass


if __name__ == '__main__':
    g = GenerateResult()
    g.get_unique_pages_list()
    print('---------------------------')
    g.longest_page_interms_of_word_count()
    print('---------------------------')
    g.display_top50_words()
    print('---------------------------')
    g.display_subdomain()
    print('---------------------------')
