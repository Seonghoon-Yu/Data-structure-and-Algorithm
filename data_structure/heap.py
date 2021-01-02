# heap 구현
class BinaryHeap(object):
    def __init__(self):
        self.items = [None] # 0번 인덱스는 사용하지 않습니다.

    def __len__(self):
        return len(self.items) - 1 # len 호출 시 마지막 index를 갖고 오기 위해 -1

    ## 삽입

    # 업힙(Up-Heap) 연산
    def _percolate_up(self):
        i = len(self) # 마지막 index 얻기
        parent = i // 2 # i의 부모 노드의 index
        while parent > 0:
            # i가 parent보다 작으면 i와 parent 스왑
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]
            # i 갱신
            i = parent
            # parent 갱신
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    ## 추출

    # 다운힙(Down-Heap) 연산
    def _percolate_down(self, idx):
        # 왼쪽 자식
        left = idx * 2
        # 오른쪽 자식
        right = idx * 2 + 1
        # 가장 작은 값
        smallest = idx

        # left와 smallest 비교
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        # right와 smallest 비교
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        # 위치 변경
        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extrack(self):
        extracted = self.items[1] # root 추출(최소값 제거)
        self.items[1] = self.items[len(self)] # 마지막 요소를 root
        self.items.pop() # 마지막 요소 제거
        self._percolate_down(1) # 다운힙(Down-Heap) 연산
        return extracted
