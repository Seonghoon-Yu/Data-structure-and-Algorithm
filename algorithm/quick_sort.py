def quick_sort(arr,L,R):
    if len(arr) <= 1:
        return arr

    def partition(L, R):
        pivot = arr[R]
        i = L-1
        for j in range(L, R):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[R] = arr[R], arr[i+1]
        return i+1
    if L < R: # 중지 조건
        pivot = partition(L,R)
        quick_sort(arr, L, pivot-1)
        quick_sort(arr, pivot+1, R)
