def merge_sort(A, desc = False):
    if len(A) <= 1:
        return A
    
    mid = len(A) // 2
    
    L = merge_sort(A[:mid], desc)
    R = merge_sort(A[mid:], desc)
    mer = []
    
    while len(L) > 0 and len(R) > 0:
        if (L[0] > R[0] and not desc) or (L[0] < R[0] and desc):
            mer.append(R[0])
        else:
            mer.append(L[0])
            
    if len(L) > 0:
        mer += L
    if len(R) > 0:
        mer += R
    return mer
