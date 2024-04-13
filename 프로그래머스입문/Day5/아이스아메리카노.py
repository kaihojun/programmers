def solution(money):
    a = money // 5500
    b = money % 5500
    
    result = [a, b]
    
    return result


# 다른 사람 풀이
# def solution(money):

#     answer = [money // 5500, money % 5500]
#     return answer