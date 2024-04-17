import math

def left_rect(h):
    result = 0
    x = 0
    steps = int(2/h)
    for i in range(0, steps):
        result += func(x)
        x = x + h
    print(f'Left rectangles with step {h}: {h*result}')
    return h*result


def euler(h):
    result1 = func(0)/2 + func(2)/2
    x = h
    steps = int(2/h)
    for i in range(0, steps-1):
        result1 += func(x)
        x = x + h
    result2 = func_diff(0)/12 - func_diff(2)/12
    print(f'Euler with step {h}: {h*result1 + (h**2)*result2}')
    return h*result1 + (h**2)*result2
    

def func(x):
    return math.sqrt(1+math.sin(x)+x**2)


def func_diff(x):
    return (2*x+math.cos(x))/(2*math.sqrt(1+math.sin(x)+x**2))

def gauss():
    return (-4/3)*func(0)+((15+2*math.sqrt(15))/9)*func(1-(math.sqrt(15)/5))+((15-2*math.sqrt(15))/9)*func(1+(math.sqrt(15)/5))
    
left_rect(0.1)
left_rect(0.05)
left_rect(0.025)

euler(0.1)
euler(0.05)
euler(0.025)

print(gauss())
