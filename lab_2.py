from math import e

E = 0.000005

FIRST = 0

def toFixed(numObj, digits=0):
    return float(f"{numObj:.{digits}f}")

def func(x):
    return toFixed(pow(e, x) - 4.6*x, 9)

def first_diff(x):
    return toFixed(pow(e, x) - 4.6, 9)

def second_diff(x):
    return toFixed(pow(e,x), 9)

def iteration(x):
    return toFixed(pow(e, x)/4.6,9)

def dichotomy(a, b):
    count = 0
    while abs(b - a) > E:
        x = toFixed((a+b)/2,9)
        if func(x)*func(b) < 0:
            a = x
        elif func(x)*func(a) < 0:
            b = x
        count+=1
    return count, x

def newton(a, b):
    count = 1
    
    x0 = FIRST
    x = toFixed(x0 - (func(x0)/first_diff(x0)), 9)
    while abs(x - x0) > E:
        x0 = x
        x = toFixed(x0 - (func(x0)/first_diff(x0)),9)
        count += 1
        
    return count, x
        

def modified_newton(a,b):
    count = 1
    
    x0 = FIRST
    m = first_diff(x0)
    x = toFixed(x0 - (func(x0)/m),9)
    while abs(x - x0) > E:
        x0 = x
        x = toFixed(x0 - (func(x0)/m),9)
        count += 1
        
    return count, x


def movable_chords(a, b, count=1, x0=FIRST):
    x1 = toFixed(a - (func(a)*(b-a)/(func(b) - func(a))),9)
    if abs(func(x1)/first_diff(x1)) > E:
        x2 = toFixed(x1-(func(x1)*(x1-x0)/(func(x1)-func(x0))),9)
        count+= 1
        while abs(func(x2)/first_diff(x2)) > E:
            x0 = x1
            x1 = x2
            x2 = toFixed(x1-(func(x1)*(x1-x0)/(func(x1)-func(x0))),9)
            count += 1
    else:
        return count, x1
    
    return count, x2


def chords(a,b, count=1, x0=FIRST):
    starting_point = FIRST

    x = toFixed(a - (func(a)*(b-a)/(func(b) - func(a))),9)
    while abs(func(x)/first_diff(x)) > E:
        x0 = x
        x = toFixed(x0 - func(x0)*(x0 - starting_point)/(func(x0) - func(starting_point)),9)
        count += 1
    return count, x
   
def simple_iteration(a,b, x0=FIRST, count=1):
    x = iteration(x0)
    while abs(x-x0)>E:
        x0 = x
        x = iteration(x0)
        count+=1
    return count, x

print(f'dichotomy: (number of iterations, answer) -> {dichotomy(0, 1)}')
print(f'newton: (number of iterations, answer) -> {newton(0, 1)}')
print(f'modified newton: (number of iterations, answer) -> {modified_newton(0, 1)}')
print(f'movable chords: (number of iterations, answer) -> {movable_chords(0, 1)}')
print(f'chords: (number of iterations, answer) -> {chords(0, 1)}')
print(f'simple iteration: (number of iterations, answer) -> {simple_iteration(0, 1)}')