from itertools import zip_longest
import sys

users_file, hobbys_file, out_file = sys.argv[1:]

with open(users_file, encoding='utf-8') as users:
    with open(hobbys_file, encoding='utf-8') as hobbys:
        users_count = sum(1 for line in users)
        hobby_count = sum(1 for line in hobbys)
        if users_count < hobby_count:
            exit(1)

        users.seek(0)
        hobbys.seek(0)

        with open(out_file, 'w+', encoding='utf-8') as file:
            for user, hobby in zip_longest(users, hobbys):
                file.write(f'{user.strip()}: {hobby.strip() if isinstance(hobby, str) else hobby}\n')

