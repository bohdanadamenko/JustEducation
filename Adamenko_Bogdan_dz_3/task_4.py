names_dict = dict()


def thesaurus_adv(*name_lastnames):
    for name_lastname in name_lastnames:
        name, lastname = name_lastname.split()
        names_dict.setdefault(lastname[0], {})
        names_dict[lastname[0]].setdefault(name[0], [])
        names_dict[lastname[0]][name[0]].append(name_lastname)
    return names_dict


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print(sorted(names_dict.items()))