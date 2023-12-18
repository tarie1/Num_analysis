EPS = 0.5*pow(10, -4)

def get_next_iteration_jacobi(x1, x2, x3):
    next_x1 = (6.77+0.11*x2 - 1.59*x3)/1.8
    next_x2 = (-3.45+0.5*x1+0.21*x3)/(-0.87)
    next_x3 = (0.82-0.61*x2-0.18*x1)/(-0.94)
    return next_x1, next_x2, next_x3

def get_next_iteration_gauss_siegel(x2, x3):
    next_x1 = (6.77+0.11*x2 - 1.59*x3)/1.8
    next_x2 = (-3.45+0.5*next_x1+0.21*x3)/(-0.87)
    next_x3 = (0.82-0.61*next_x2-0.18*next_x1)/(-0.94)
    return next_x1, next_x2, next_x3

def method_Jacobi():
    prev_x1 = 6.77/1.8
    prev_x2 = (-3.45)/(-0.87)
    prev_x3 = 0.82/(-0.94)
    
    next_x1, next_x2, next_x3 = get_next_iteration_jacobi(prev_x1, prev_x2, prev_x3)
    count = 1
    
    while abs(prev_x1-next_x1)>EPS and abs(prev_x2-next_x2)>EPS and abs(prev_x3-next_x3)>EPS:
        prev_x1 = next_x1
        prev_x2 = next_x2
        prev_x3 = next_x3
        next_x1, next_x2, next_x3 = get_next_iteration_jacobi(prev_x1, prev_x2, prev_x3)
        count += 1
        
    print(f'Method Jacobi:\nx1 = {next_x1}, x2 = {next_x2}, x3 = {next_x3}. \nNumber of iterations = {count}')
    
def method_gauss_seidel():
    prev_x1 = 6.77/1.8
    prev_x2 = (-3.45+0.5*prev_x1)/(-0.87)
    prev_x3 = (0.82-0.18*prev_x1-0.61*prev_x2)/(-0.94)
    count = 1
    next_x1, next_x2, next_x3 = get_next_iteration_gauss_siegel(prev_x2, prev_x3)
    while abs(prev_x1-next_x1)>EPS and abs(prev_x2-next_x2)>EPS and abs(prev_x3-next_x3)>EPS:
        prev_x1 = next_x1
        prev_x2 = next_x2
        prev_x3 = next_x3
        next_x1, next_x2, next_x3 = get_next_iteration_gauss_siegel(prev_x2, prev_x3)
        count += 1
        
    print(f'Method Gauss-Siegel:\nx1 = {next_x1}, x2 = {next_x2}, x3 = {next_x3}. \nNumber of iterations = {count}')
    

method_Jacobi()
method_gauss_seidel()
