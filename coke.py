
cost = 50
paid = 0

def check_coin(c):
    is_coin = False
    if c == 1 or c == 5 or c == 10 or c == 25:
        is_coin = True
    return is_coin



while cost > paid:
    print(f'Amount Due: {cost - paid}')
    a = input('Insert Coin: ')
    coin = int(a)
    is_coin = check_coin(coin)

    if is_coin:
        paid += coin
    
    if cost < paid:
        print(f'Change Due: {paid - cost}')

    
    