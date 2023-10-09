def swap_biggest_and_lowest(arr):
    result = arr
    min = max = arr[0]
    min_index = max_index = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
        if arr[i] > max:
            max = arr[i]
            max_index = i
    result[min_index], result[max_index] = result[max_index], result[min_index]
    
    return result

arr = list(map(float, input().split()))

print(swap_biggest_and_lowest(arr))
