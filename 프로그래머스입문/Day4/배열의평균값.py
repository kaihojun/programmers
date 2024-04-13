def solution(numbers):
    total = 0
    for i in numbers:
        total += i
    avg = total / len(numbers)
    
    return avg

# 다른 사람 풀이 1
# import numpy as np
# def solution(numbers):
#     return np.mean(numbers)
#
# 다른 사람 풀이 2
# def solution(numbers):
#     return sum(numbers) / len(numbers)