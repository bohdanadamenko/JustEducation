import re
EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    try:
        found_info = EMAIL.findall(email)[0]
    except:
        found_info = None
    if found_info:
        name, addr = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    return {'username': name, 'domain': addr}



print(email_parse('adamenko.bogdan@gmail.com'))
print(email_parse('adamenko.bogdangmail.com'))