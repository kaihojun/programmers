# ■ count() 함수 :
# - 튜플, 리스트, 집합과 같은 반복 가능한 iterable 자료형에서 사용 가능
# - 변수.count(찾는 요소) 형태로 사용
# - 괄호 안에 찾고자 하는 값을 입력하면 함수를 사용한 변수 안에서 해당 값의 개수를 숫자로 반환

# ■ set(집합) 함수 :
# 여기에서는 set() 함수를 사용하여 중복값을 제거해주었다.

def solution(array):
    answer = 0
    set_array = set(array)

    max_count = 0
    for i in set_array:
        count = array.count(i)

        if count > max_count:
            max_count = count
            answer = i
        elif count == max_count:
            answer = -1

    return answer        


array = [1,1,2,2]
print(solution(array))


# 다른 사람 풀이(좋아요 1등)
# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1