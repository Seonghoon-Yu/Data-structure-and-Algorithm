def quick_sort(A, lo, hi): # A: 배열, lo: 시작 인덱스, hi: 마지막 인덱스
    # 파티션 분할 함수 정의
    def partition(lo, hi):
        pivot = A[hi] # 오른쪽 맨 끝을 pivot으로 선정
        left = lo
        
        for right in range(lo, hi):
            if A[right] < pivot: # right가 pivot보다 작으면 left와 right 값 변경
                A[right], A[left] = A[left], A[right]
                left += 1 # left 1칸 이동
        A[left], A[hi] = A[hi], A[left] # left와 pivot 위치 변경
        return left
    pivot = partition(lo, hi)
    quick_sort(A, lo, pivot - 1)
    quick_sort(A, pivot + 1, hi)
