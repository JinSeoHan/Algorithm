def solution(s):
    nums = list(map(int, s.split()))
    answer = f'{min(nums)} {max(nums)}'
    return answer