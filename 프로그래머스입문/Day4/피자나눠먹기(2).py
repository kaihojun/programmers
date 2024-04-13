def solution(n):
    num = 1
    while(True):
        if (n * num)  %  6 != 0:
            num += 1
        elif (n * num) % 6 == 0:
            return (n * num) // 6
        
# 다른 사람 풀이
# def solution(n):
#     num = 1
    
#     while(True):
#         if (6*num) % n == 0:
#             return num
#         else:
#             num += 1