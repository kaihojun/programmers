# 몫 구하기

# 내 풀이
def solution(num1, num2):
    answer = int(num1 / num2)
    return answer

# 다른 사람 풀이
def solution(num1, num2):
    answer = num1 // num2
    return answer

# 다른 사람 풀이 2
# 기본 정의된 연산자 메서드 이용. 연산자 오버로딩시에 쓰임
solution = int.__floordiv__

# 다른 사람 풀이 2를 보고 푼 내 풀이
def solution(num1, num2):
    solution = num1.__floordiv__(num2)
    return solution

"""
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()
"""