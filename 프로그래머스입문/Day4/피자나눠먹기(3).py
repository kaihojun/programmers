def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return (n//slice) + 1
    

# 다른 사람 풀이
# def solution(slice, n):
#     return (n-1)//slice + 1