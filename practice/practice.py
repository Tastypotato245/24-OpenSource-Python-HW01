import random

def Game():
    dab = random.randint(1, 9)

    life = 3

    while life > 0 :
        number = int(input('Enter N> '))

        if number > dab :
            print('DOWN')
        if number < dab :
            print('UP')
        if number == dab :
            print('GOOD')
            return

        life = life - 1

    print('LOSE')

Game()
