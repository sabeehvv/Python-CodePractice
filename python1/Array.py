def reverse(arr):
    n = len(arr)-1
    start = 0
    end = n

    while start < end :
        arr[start] ,arr[end] = arr[end] ,arr[start]

        start += 1
        end -= 1

arr = [1,7,6,3,4]

print('original array',arr)

reverse(arr)

print(arr)