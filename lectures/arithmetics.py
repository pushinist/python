def summator(a, b):
    print(f"{a} + {b} = {a + b}")
    pass


def multiplicator(a, b):
    print(f"{a} * {b} = {a * b}")
    pass


pi = 3.14

# Выполняется исключительно в случае запуска программы конкретно с этого файла, а не его импорта
if __name__ == "__main__": 
    summator(1, 4)
    multiplicator(10, 2)


