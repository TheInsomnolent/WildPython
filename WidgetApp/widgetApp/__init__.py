import time 
import random

'''
    We split our API calles into the __init__.py file so they 
    can be easily imported by our users
'''

def buyWidget():
    '''Buy a widget through some fake API call'''
    cost = random.randint(1, 10)
    return cost


def sellWidget():
    '''Sell a widget through some fake API call'''
    price = random.randint(2, 11)
    return price


