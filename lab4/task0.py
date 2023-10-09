def more_than_previous(arr):
    res = []
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            res.append(arr[i + 1])
    return res



arr = list(map(float, input().split()))
print(more_than_previous(arr))
