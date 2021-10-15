from random import randint

def d2():
    return randint(1,2)

def d4():
    return randint(1,4)

def d6():
    return randint(1,6)

def d8():
    return randint(1,8)

def d10():
    return randint(1,10)

def d12():
    return randint(1,12)

def d20():
    return randint(1,20)

def d100():
    return randint(1,100)

def roll(n,d):
    return [d() for x in range(n)]

def sum_roll(n,d):
    return sum([d() for x in range(n)])

def rolld20(target, n_dices, focus = 0, difficulty = 1):
    result = roll(n_dices,d20)
    successes = 0
    complications = 0
    for r in result:
        if r <= focus:
                successes += focus
        
        elif r <= target:
            successes += 1
            
        if r == 20:
            complications += 1

    momentum = successes - difficulty
    if momentum >= 0:
        return ('success',successes, momentum, complications)
    
    return ('failure', successes, 0, complications) 


        

