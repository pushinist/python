'''
Есть текстовый файл, в котором содержатся строки вида
название_товара цена акция
Первый элемент — str
Второй элемент — int
Третий элемент — bool
Надо прочитать оттуда всю эту информацию, записать в виде кортежей, поместить их в список, 
отсортировать по названию товара в алфавитном порядке, а потом выгрузить обратно в новый текстовый файл 
и новый бинарный файл (в виде байтов). Про текстовые файлы вы потом забываете, 
а вот только что сформированный бинарный файл открываете на чтение, читаете из него информацию, 
превращаете её обратно в кортежи, помещаете в список и сортируете его по возрастанию цены 
и записываете всё в новый (уже третий по счёту) текстовый файл.
'''


with open(r'text.txt', 'r', encoding='utf-8') as file:
    data = []
    for line in file:
        data.append(tuple(line.split()))
    result = sorted(data, key=lambda tuple: tuple[0])

with open(r'output_text.txt', 'w', encoding='utf-8') as file:
    for line in result:
        for item in line:
            file.write(item)
            file.write('\t')
        file.write('\n')



with open(r'output_bin.bin', 'wb') as file:
    for line in result:
        for item in line:
            #print(type(bytes(item, encoding='utf-8')))
            file.write(bytes(item, encoding='utf-8'))
            file.write(b'\t')
        file.write(b'\n')

with open(r'output_bin.bin', 'rb') as file:
    data = []
    for line in file:
        data.append(tuple(line.split()))
    result = sorted(data, key=lambda tuple: tuple[2])

with open(r'output_bin.txt', 'w', encoding='utf-8') as file:
    for line in result:
        for item in line:
            file.write(str(item))
            file.write('\t')
        file.write('\n')