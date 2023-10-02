def get_rows(n):
    rows = [[1]]
    for i in range(1, n):
        tmp_row = [1]
        for j in range(1, i):
            tmp_row.append(rows[i - 1][j] + rows[i - 1][j - 1])
        tmp_row.append(1)
        rows.append(tmp_row)
    return rows


n = int(input())
rows_amount = 2 ** n
rows = get_rows(rows_amount)

for i in range(1, len(rows)):
    for j in range(1, len(rows[i]) - 1):
        rows[i][j] = (rows[i - 1][j - 1] + rows[i - 1][j]) % 2

for i in range(len(rows)):
    print(' ' * (rows_amount - 1 - i), end='')
    for j in rows[i]:
        if j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()