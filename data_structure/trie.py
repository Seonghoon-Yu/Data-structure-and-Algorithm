# 트라이를 저장할 노드를 별도 클래스로 선언
class TrieNode:
    def __init__(self):
        self.word = False # 각각의 노드는 word 값을 갖는다.
        self.children = collections.defaultdict(TrieNode) # 자식의 기본값은 TrieNode

# 트라이 클래스 선언
class Trie:
    def __init__(self):
        # 루트 노드 생성
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                # char 순서대로 자식 노드 추가
                node.children[char] = TrieNode()
            # 자식 노드를 타고 내려가기
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word):
        node = self.root
        # 자식 노드를 타고 내려가면서 node.word 여부 리턴
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            # 자식 노드 여부 판별
            if char not in node.children:
                return False
            node = node.children[char]

        return True
