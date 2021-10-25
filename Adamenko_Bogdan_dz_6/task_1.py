import requests

link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = requests.get(link).text
table = []

with open('nginx_logs.txt', 'w+') as file:
    file.write(response)
    file.seek(0)
    line = file.readline()

    for line in file:
        remote_addr = line[0:line.find(' ')]
        request_type = line[line.find('GET'):line.find('GET') + len('GET')]
        requested_resource = line[line.find('/', line.find('GET') + len('GET')):line.find(' ', line.find('/', line.find('GET') + len(
                    'GET')))]
        info = (remote_addr, request_type, requested_resource)
        table.append(info)

print(table)