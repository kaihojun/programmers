import math

# 최대 공약수 : gcd()
# 최소 공배수 : lcm()

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    num = math.gcd(numer, denom)
    
    numer = int(numer / num)
    denom = int(denom / num)
        
    answer = [numer, denom]
    return answer