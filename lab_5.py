import matplotlib.pyplot as plt
import math

def get_step(N):
    return 1/N


def func(x,y):
    return -((x-1)/y)


def diff_func(x):
    return math.sqrt(2*x-(x**2)+4)


def diff_funcX(y):
    return -1/y


def diff_funcY(x,y):
    return -(x-1)/(y**2)


def graph_coorX(N):
    x_coor = []
    x = float(1/N)
    for i in range(0,N):
        x_coor.append(math.floor(x*i*100)/100)
    return x_coor


def accurate(N, x_coor):
    y_coor = []
    for i in range(0, N):
        y_coor.append(diff_func(x_coor[i]))
    return y_coor


def euler(N, x_coor):
    y_coor = [2]
    h = get_step(N)
    for i in range(1, N):
        y_coor.append(y_coor[i-1] + h*func(x_coor[i-1], y_coor[i-1]))
    return y_coor


def taylor(N, x_coor):
    y_coor = [2]
    h = get_step(N)
    for i in range(1, N):
        y_coor.append(y_coor[i-1] + h*func(x_coor[i-1], y_coor[i-1]) + (h**2/2)*
                      (diff_funcX(y_coor[i-1])+func(x_coor[i-1], y_coor[i-1])*diff_funcY(x_coor[i-1], y_coor[i-1])))
    return y_coor


def adams(N, x_coor):
    y_coor = [2]
    h = get_step(N)
    y_coor.append(y_coor[0] + h*func(x_coor[0], y_coor[0]) + (h**2/2)*
                      (diff_funcX(y_coor[0])+func(x_coor[0], y_coor[0])*diff_funcY(x_coor[0], y_coor[0])))
    for i in range(2, N):
        y_coor.append(y_coor[i-1] + (h/2)*(3*func(x_coor[i-1], y_coor[i-1]) - func(x_coor[i-2], y_coor[i-2])))
    return y_coor


x_coor30 = graph_coorX(30)

plt.plot(x_coor30, accurate(30, x_coor30), color='deeppink')
plt.plot(x_coor30, euler(30, x_coor30), color='forestgreen')
plt.plot(x_coor30, taylor(30, x_coor30), color='deepskyblue')
plt.plot(x_coor30, adams(30, x_coor30), color='darkviolet')
plt.legend(['Accurate', 'Euler', 'Taylor', 'Adams'], loc=2)
plt.title('Comparison')
plt.grid(True)
plt.show()


