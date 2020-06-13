from random import randint
##Simulates a D20 roll, and identifies critical hits and misses
def d20_roller ():
    d20Min = 1
    d20Max = 20

    d20Roll = randint(d20Min, d20Max)
    if d20Roll == 20:
        print('It\'s a critical hit! You rolled ' + str(d20Roll))
    elif d20Roll == 1:
        print('Oof, it\'s a critical miss. You rolled ' + str(d20Roll))
    else:
        print('You rolled ' + str(d20Roll))
# Simulates a D12 roll
def d12_roller ():
    d12Min = 1
    d12Max = 12

    d12Roll = randint(d12Min, d12Max)
    print('You rolled ' + str(d12Roll))
       
def d10_roller ():
    d10Min = 1
    d10Max = 10

    d10Roll = randint(d10Min, d10Max)
    print('You rolled ' + str(d10Roll))

def d8_roller ():
    d8Min = 1
    d8Max = 8

    d8Roll = randint(d8Min, d8Max)
    print('You rolled ' + str(d8Roll))

def d6_roller ():
    d6Min = 1
    d6Max = 6

    d6Roll = randint(d6Min, d6Max)
    print('You rolled ' + str(d6Roll))

def d4_roller ():
    d4Min = 1
    d4Max = 4

    d4Roll = randint(d4Min, d4Max)
    print('You rolled ' + str(d4Roll))
       


d20_roller()
d10_roller()
