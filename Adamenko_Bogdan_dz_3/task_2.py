numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
           'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
           'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(n):
    if n.istitle():
        return numbers.get(n.lower()).title()
    else:
        return numbers.get(n)


print(num_translate('one'),
      num_translate('One'),
      num_translate('1'))
