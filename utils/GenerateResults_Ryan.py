import re
from urllib.parse import urlparse


unique_urls = dict()

with open('tmp/unique_file_urls.txt') as f:
    f.readline()

    for line in f:
        l = line.strip()

        if l not in unique_urls:
            unique_urls[l] = 0
        unique_urls[l] += 1

print(f"Unique URLs: {len(unique_urls)}")

three_counts = 0
two_counts = 0

for url in unique_urls:
    if unique_urls[url] == 3:
        three_counts += 1
    elif unique_urls[url] == 2:
        two_counts += 1

print(f"URLs appearing 3 times: {three_counts}")
print(f"URLs appearing twice: {two_counts}\n")


pattern = re.compile(r".*\.ics\.uci\.edu")
port_number = re.compile(r".*(:\d+)$")

subdomains = dict()

for url in unique_urls:
    if pattern.match(url):

        # lower the domain bc hosts are case insensitive
        domain = urlparse(url).netloc.lower()

        # some domains have www at the beginning, remove that
        if 'www.' == domain[:4]:
            domain = domain[4:]

        # # some domains have the port number at the end, remove that
        m = port_number.match(domain)
        if m:
            domain = domain[: domain.index(m.group(1))]

        if domain not in subdomains:
            subdomains[domain] = 0
        subdomains[domain] += 1

print(f"Subdomains under ics.uci.edu: {len(subdomains)}")

for domain in sorted(subdomains):
    print(f"{domain} -> {subdomains[domain]}")
