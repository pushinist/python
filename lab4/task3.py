def repeated_strings(arr):
    result = dict()
    for x in arr:
        result[x] = result.get(x, 0) + 1
    return result

arr = list(input().split())

print(*list(repeated_strings(arr).values()))
