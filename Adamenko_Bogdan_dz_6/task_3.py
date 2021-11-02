import json
from itertools import zip_longest

people_dict = dict()
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobbys:
        users_count = sum(1 for line in users)
        hobby_count = sum(1 for line in hobbys)
        if users_count < hobby_count:
            exit(1)

        users.seek(0)
        hobbys.seek(0)

        for user, hobby in zip_longest(users, hobbys):
            people_dict[user.strip()] = hobby.strip() if hobby is not None else hobby

print(people_dict)


with open('task_3.json', 'w+', encoding='utf-8') as file:
    json.dump(people_dict, file, ensure_ascii=False)
    file.seek(0)
    print(*file)
