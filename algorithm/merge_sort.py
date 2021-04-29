import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = merge_sort(arr[:mid]) # 분할
    R = merge_sort(arr[mid:]) # 분할
    mer = []

    i = 0
    j = 0
    while i < len(L) and j < len(R): # 정렬 및 결합
        if (L[i] > R[j]):
            mer.append(R[j])
            j += 1
        else:
            mer.append(L[i])
            i += 1

    if i != len(L):
        mer += L[i:]
    if j != len(R):
        mer += R[j:]
    return mer

mer = merge_sort(arr)
for i in mer:
    print(i)
