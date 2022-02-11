import csv
import os


class GenerateResult:
    def __init__(self):
        self.top50Word = {}

    def get_unique_pages_list(self):
        cnt = 0
        with open('../tmp/unique_file_urls.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                cnt += 1
        print("Count of Unique URLS visted : ", (cnt - 1))

    def get_subdomains(self):
        pass

    def get_longest_page(self):
        pass

    def get_top50_words(self):
        pass

    def read_file(self):
        path = '../tmp/pg_index_example.txt'
        if not os.path.isfile(path):
            print('ERROR :: Something went wrong file does not exist.')
            return
        cnt = 3
        max_size_page, max_size_url = 0, ''
        with open(path, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter='\t')
            for row in reader:
                print(type(row))
                if int(row[0]) > max_size_page:
                    max_size_page = int(row[0])
                    max_size_url = row[2]

                if cnt == 0:
                    break
                cnt -= 1

        print('Max sized page: ', max_size_page)
        print('URL: ', max_size_url)


if __name__ == '__main__':
    g = GenerateResult()
    g.get_unique_pages_list()
    g.read_file()
