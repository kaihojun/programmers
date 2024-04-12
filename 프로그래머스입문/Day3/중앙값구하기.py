def solution(array):
    array = sorted(array)
    num = int(len(array) / 2)
    
    return array[num]