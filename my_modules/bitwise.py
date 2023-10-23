def bitwise_sum(a, b):
    print(f"{a} | {b} = {a | b}")


def bitwise_mult(a, b):
    print(f"{a} & {b} = {a & b}")


# Выполняется исключительно в случае запуска программы конкретно с этого файла, а не его импорта
if __name__ == "__main__": 
    bitwise_sum(1, 4)
    bitwise_mult(10, 2)


