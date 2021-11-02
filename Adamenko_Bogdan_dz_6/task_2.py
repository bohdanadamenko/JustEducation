import requests

link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = requests.get(link).text
spamer = dict()

with open('nginx_logs.txt', 'w+') as file:
    file.write(response)
    file.seek(0)
    line = file.readline()

    for line in file:
        remote_addr = line[0:line.find(' ')]
        spamer.setdefault(remote_addr, 0)
        spamer[remote_addr] += 1

sorted_spamers = sorted(spamer.items(), key=lambda x: x[1], reverse=True)
print(sorted_spamers[:3])
