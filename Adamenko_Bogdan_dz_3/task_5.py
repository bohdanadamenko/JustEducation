import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes_list = []


def get_jokes(cycles, repeats=True):
    """function has generate random joke"""
    if not repeats:
        if cycles > min(len(nouns), len(adverbs), len(adjectives)):
            return 'that impossible'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(cycles):
                jokes_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(cycles):
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            jokes_list.append(f'{noun} {adverb} {adjective}')
    return jokes_list


print(get_jokes(7, True))
print(get_jokes(7, False))
print(get_jokes(4, True))
