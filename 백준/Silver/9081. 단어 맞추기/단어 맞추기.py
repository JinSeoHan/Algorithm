'''
next permutation algorithm
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word = list(input().strip())

    # 첫 번째 피벗 포인트
    flag = False
    for i in range(len(word)-2, -1, -1):
        if ord(word[i]) < ord(word[i+1]):
            pivot = i
            # 피벗 포인트보다 큰 값중 가장 작은 값을 가지는 지점을 찾는다.
            jpoint = [0,100000]
            for j in range(len(word)-1, pivot-1, -1):
                if ord(word[pivot]) < ord(word[j]) and jpoint[1] > ord(word[j]):
                    jpoint[0], jpoint[1] = j, ord(word[j])
                    flag = True
            # 위치를 변경한다.
            word[pivot], word[jpoint[0]] = word[jpoint[0]], word[pivot]
            # 피벗 기준 오른쪽 요소 오름차순 정렬
            word = word[:pivot+1]+sorted(word[pivot+1:])
            print(''.join(word))
            break
        if flag: break
    if not flag:
        print(''.join(word))