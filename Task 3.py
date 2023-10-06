def number_to_words(n):
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    h = {100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
         500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот',
         800: 'восемьсот', 900: 'девятьсот'}
    if n < 100:
        n1 = n % 10
        n2 = n - n1
    if n >= 100:
        n1 = n % 10
        n2 = (n // 10 % 10) * 10
        n3 = n - n2 - n1
    if n == 1000:
        return "тысяча"
    elif n < 10:
        return f.get(n)
    elif 10 < n < 20:
        return s.get(n)
    elif n >= 10 and n in o:
        return o.get(n)
    elif n < 100:
        return o.get(n2) + ' ' + f.get(n1)
    elif n >= 100 and n in h:
        return h.get(n3)
    elif n // 10 % 10 == 0:
        return h.get(n3) + ' ' + f.get(n1)
    elif n >= 110 and (n - n3) in s:
        return h.get(n3) + ' ' + s.get(n - n3)
    elif n % 10 == 0:
        return h.get(n3) + ' ' + o.get(n2)
    else:
        return h.get(n3) + ' ' + o.get(n2) + ' ' + f.get(n1)

for i in range(1001):
    print(f"{i} - {number_to_words(i)}")
