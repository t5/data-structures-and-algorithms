from collections import defaultdict

def new_m(lower, upper):
    return (lower+upper)/2.0

def square(n):
    lower = 1
    upper = n
    middle = new_m(lower, upper) 

    answers = defaultdict(lambda: False)
    while True:
        if middle**2 < n:
            lower = middle
        else:
            upper = middle
        middle = new_m(lower, upper)
        
        # checks if the answer is final
        if answers[middle] == True:
            print(middle**2)
            break
        else:
            answers[middle] = True

square(1234567891012345678910500012345678910)
