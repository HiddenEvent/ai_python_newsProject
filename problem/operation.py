# DFS(깊이우선탐색)를 알아야 풀수있음 DFS를 알아보자

# 핵심 순서
# 1. 연산자 부분을 람다 배열로 만들어 연산 갯수만큼 하나의 리스트를 만드는 부분 생각...

# 1. 연산자가 들어갈 수 있는 모든 경우의 수 먼저 구한다.
#   - 팩토리얼로 구할 수 있음 ex) 5의 팩토리얼은 120 / 2 (중복제거)
import itertools
from functools import reduce
import sys


def OperatorCalc(length, input_num, input_oper):
    ops = {"0": (lambda x, y: x + y), "1": (lambda x, y: x - y), "2": (lambda x, y: x * y),
           "3": (lambda x, y: x // y if x > 0 else -(-x // y))}
    oper_permutation = []
    result = []
    list(oper_permutation.extend(
        [str(index)] * value) for index, value in enumerate(input_oper) if value > 0)

    # itertools.permutations() 은 배열안의 모든 경우의 수 배열들을 가져온다.
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]

    for i in permutation:
        result.append(reduce(lambda x, y: ops[i.pop()](x, y), input_num))
    return int(max(result)), int(min(result))


if __name__ == "__main__":
    length = int(sys.stdin.readline())
    if 2 <= length <= 11:
        input_num = [int(x) for x in sys.stdin.readline().split()]
        input_oper = [int(x) for x in sys.stdin.readline().split()]

    max, min = OperatorCalc(length, input_num, input_oper)
    print(max)
    print(min)
