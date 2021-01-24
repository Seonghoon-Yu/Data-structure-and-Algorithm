# 배낭에 담을 수 있는 무게의 최댓값(15kg)이 정해져 있고
# 각각 짐의 가치와 무게가 있는 짐들을 넣을 떄 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제

# 짐(cargo)를 (가치, 무게) 순으로 튜플 리스트 정의
cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]

def fractional_knapsack(cargo):
    capacity = 15
    back = []
    for c in cargo:
        back.append((c[0]/c[1], c[0], c[1]))
    back.sort(reverse=True)

    total_value = 0
    for b in back:
        if capacity - b[2] > 0:
            capacity -= b[2]
            total_value += b[1]
        else:
            fraction = capacity / b[2]
            total_value += fraction * b[1]
            break
    return total_value
