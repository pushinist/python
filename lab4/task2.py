def compare(arr1, arr2):
    res = set()
    for item1 in arr1:
        for item2 in arr2:
            if item1 == item2:
                res.add(item1)
    return list(res)


arr1 = list(map(float, input().split()))
arr2 = list(map(float, input().split()))

print(compare(arr1, arr2))

