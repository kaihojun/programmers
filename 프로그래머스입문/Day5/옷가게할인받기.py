def solution(price):
    if 100000 <= price and price < 300000:
        return int(price - (price * 0.05))
    elif 300000 <= price and price < 500000:
        return int(price - int(price * 0.1))
    elif price >= 500000:
        return int(price - int(price * 0.2))
    else:
        return int(price)
    


# 다른 사람 풀이(딕셔너리 사용)
# def solution(price):
# discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
# for discount_price, discount_rate in discount_rates.items():
#     if price >= discount_price:
#         return int(price * discount_rate)