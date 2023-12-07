import pymorphy2

morph = pymorphy2.MorphAnalyzer()
print(morph.parse('Ваня'))

res = morph.parse('Питона')[1]
print(res)
print("VERB" in res.tag)
print("accs" in res.tag)
print({'NOUN', 'accs'} in res.tag)

res = morph.parse('Писал')[0]
print(res.tag.mood)
print(res.tag.tense)
print(res.tag.case)

res = morph.parse('книга')
w1 = res[0]
w2 = w1.inflect({'accs', 'plur'})
print('Не забывайте свои', w2.word)
w3 = w1.inflect({'accs'})
print(w3)

# Задача: придумать фразу, состоящую из нескольких предложений, чтобы в этих предложениях
# попросить пользователя ввести с клавиатуры несколько слов (хотя бы 1 сущ, прил, гл.) и вставить введеные пользователем
# слова в шаблон предложения так, чтобы получилось грамматически верное предложение
# Плохого человека {w} не назовут. Обладая тысячью {w}, он{w} может создать {adj} {noun}.
# Ввод: Олег, рубль, шикарный, вилла
# Вывод: Плохого человека Олегом не назовут. Обладая тысячью рублей, он может создать шикарную виллу.


# 1) docx template (формат JINJA)