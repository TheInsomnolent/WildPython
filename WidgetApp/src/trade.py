import time 
import random

def buyWidget():
    '''Buy a widget through some fake API call'''
    cost = random.randint(1, 10)
    return cost


def sellWidget():
    '''Sell a widget through some fake API call'''
    price = random.randint(2, 11)
    return price


def main():
    capital = 100
    print(f'We started widget trading with ${capital}')

    for _ in range(1000):
        capital -= buyWidget()
        capital += sellWidget()
    
    print(f'We closed widget trading with ${capital}')



if __name__ == "__main__":
    main()