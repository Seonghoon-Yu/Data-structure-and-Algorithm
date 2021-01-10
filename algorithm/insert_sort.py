def insert_sort(A): 
    for i in range(1, len(A)):
        insert = A[i] # insert 값 지정
        j = i # 비교를 위해 j 지정
        while j > 0 and A[j-1] > insert: # j가 0보다 크고, j-1이 insert보다 크면 실행
            A[j-1] = A[j] # A[j-1]를 A[j]로 선정하여 공간 확보
            j -= 1        # j값 갱신
        A[j] = insert     # [j-1]보다 크면 [j]값에 insert 값 지정
