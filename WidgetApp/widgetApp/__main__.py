from widgetApp import buyWidget, sellWidget


'''
    We put our runscript into the __main__.py file so it is only executed 
    when the module is run and not when the module is imported
'''


def main():
    capital = 100
    print(f'We started widget trading with ${capital}')

    for _ in range(1000):
        capital -= buyWidget()
        capital += sellWidget()
    
    print(f'We closed widget trading with ${capital}')



if __name__ == "__main__":
    main()