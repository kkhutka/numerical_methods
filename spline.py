# import math 
# import numpy as np
# import matplotlib.pyplot as plt


# def mainFunc(x):
#     return np.power(x,2) + np.sin(x) * np.cos(x)*np.exp(x)


# def linear_splines(x_i, y_i, x):
#     result=0
#     for i in range(len(x_i)-1):
#        if x_i[i] <= x <= x_i[i + 1]:
#             return (x-x_i[i])*(y_i[i+1]-y_i[i])/(x_i[i+1]-x_i[i])+y_i[i]
#     return None

# def cubic_spline(x, y, t):


#     n = len(x)
#     h = [x[i + 1] - x[i] for i in range(n - 1)]
#     F = [(3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1])
#               * (y[i] - y[i - 1]) for i in range(1, n - 1)]

#     znam = [1.0] * n
#     alpha = [0.0] * n
#     beta = [0.0] * n

    
#     for i in range(1, n-1):
#         znam[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * znam[i - 1]
#         alpha[i] = (h[i] / znam[i])
#         beta[i] = (F[i - 1] - h[i - 1] * beta[i - 1]) / znam[i]

#     c = [0.0] * n

#     for j in range(n - 2, 0, -1):
#         c[j] = beta[j+1] + alpha[j+1] * c[j + 1]

#     b = [(y[i + 1] - y[i]) / h[i] - h[i] *
#          (c[i + 1] + 2 * c[i]) / 3.0 for i in range(n - 1)]
#     d = [(c[i + 1] - c[i]) / (3.0 * h[i]) for i in range(n - 1)]

#     s=0
#     for i in range(0,n-1):
#         if x[i]<=t<=x[i+1]:
#             s=y[i]+b[i]*(t-x[i])+c[i]*pow(t-x[i],2)+d[i]*pow(t-x[i],3)
#     return s


# a = float(input("Введіть а: "))
# b = float(input("Введіть b: "))
# n = int(input("Введіть n: "))

# x_i=np.linspace(a,b,n)
# y_i=mainFunc(x_i)


# x_interp=np.linspace(a,b,1000)
# y_interp_lin = [linear_splines(x_i, y_i, xi) for xi in x_interp]

# y_interp_cubic=[cubic_spline(x_i, y_i, xi) for xi in x_interp]

# plt.figure(figsize=(16, 8))
# plt.scatter(x_i, mainFunc(x_i), color='red', label='Nodes', marker='o', zorder=10)
# plt.plot(x_interp, mainFunc(x_interp), label='sin(x)')
# plt.plot(x_interp, y_interp_lin, label='лінійний B-сплайн')
# plt.plot(x_interp, y_interp_cubic, 'b-', label='кубічний B-сплайн')
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Cubic B-Spline Interpolation')
# plt.grid()
# plt.show()



# # interpolated_x = np.linspace(0, 2 * np.pi, 1000)
# # y, b, c, d = cubic_b_spline_interpolation(x, y)

# # interpolated_y = []
# # interpolatedy = np.linspace(0, 2 * np.pi, 1000)
# # # Розраховуємо значення інтерпольованої кривої на кожному сегменті
# # for i in range(len(x) - 1):
# #     mask = (interpolated_x >= x[i]) & (interpolated_x <= x[i + 1])
# #     x_sub = interpolated_x[mask] - x[i]
# #     y_sub = y[i] + b[i] * x_sub + c[i] * x_sub ** 2 + d[i] * x_sub ** 3
# #     interpolated_y.extend(y_sub)
# # for i in range(len(interpolated_x)):
# #     interpolatedy[i] = interpolated_y[i]

# # xv = np.linspace(0, 2 * np.pi, 1000)
# # yv = f(xv)

# # # Генеруємо точки для побудови B-сплайна
# # x_spline = np.linspace(0, 2 * np.pi, 100)
# # y_spline = [linear_b_spline(x, y, t) for t in x_spline]

# # # Малюємо графіки
# # plt.figure(figsize=(16, 8))
# # plt.plot(x, y, 'o', label='т.')
# # plt.plot(xv, yv, label='sin(x)')
# # plt.plot(interpolated_x, interpolatedy, label='кубічна B-сплайн')
# # plt.plot(x_spline, y_spline, 'b-', label='лінійний B-сплайн')
# # plt.legend()
# # plt.xlabel('X')
# # plt.ylabel('Y')
# # plt.title('Cubic B-Spline Interpolation')
# # plt.grid()
# # plt.show()


# linear_interpolation_values = [linear_b_spline(t, x) for t in (t_values)]
# plt.figure(figsize=(10, 6))
# plt.plot(t_values, f_values, label='f(x)',linewidth =10, zorder=0)
# plt.plot(t_values, linear_interpolation_values, label='Linear Interpolation', linewidth =5, zorder = 1 )
# plt.plot(t_values, cubic_interpolation_values, label='Cubic Interpolation', linewidth = 3, zorder = 2
#          )
# plt.scatter(x, [f(xi) for xi in x], color='red', label='Nodes', marker='o', zorder=10)  # Відображення вузлів
# plt.scatter(max_error_point, f(max_error_point), color='green', label='Max Error Point')
# plt.legend()
# plt.title('Interpolation with B-splines')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)

# plt.show()


from ast import BitAnd
import numpy as np
import matplotlib.pyplot as plt

def B1(x):
    if abs(x) <= 1:
        return 1 - abs(x)
    else:
        return 0
    
def B2(x):
    if abs(x) < 1:
        return 1/6((2 - abs(x))**3-4*(1-abs(x))**3)
    elif (1 <= abs(x) <2):
        return 1/6((2 - abs(x))**3)
    else:
        return 0

f = lambda x: np.power(x, 2)

def linear_b_spline(x_i, x, y):
    return sum([y[k] * B1((x_i - x[k]) / (x[1] - x[0])) for k in range(len(y))])

a = 0
b = 10
n = 5

x = np.linspace(a, b, n)
y = f(x)

x_for_graph = np.linspace(a, b, 1000)
y_for_graph = f(x_for_graph)

# Evaluate the linear beta-spline for the x values
y_spline = [linear_b_spline(xi, x, y) for xi in x_for_graph]

plt.figure(figsize=(8, 6))
plt.plot(x_for_graph, y_for_graph, label='Original Function')
plt.plot(x_for_graph, y_spline, label='Linear Beta-Spline')
plt.scatter(x, y, c='red', label='Data Points', marker='o')
plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Beta-Spline Interpolation')
plt.show()
    
result=[0.0]*n
A= [1/6]*n
B= [1/6]*n
C= [2/3]*n
C[0]=-0.5
B[0]=0.5
A[n-1]=-0.5
C[n-1]=0.5
alpha=[0.0]*n
alpha[0]=-B[0]/C[0]

F=y
F[0]=(x[1]-x[0])*a
F[n-1]=(x[1]-x[0])*b
beta=[0.0]*n
beta[0]=F[0]/C[0]
for i in range(1, n-1):
        alpha[i] = -B[i]/(C[i]+A[i]*alpha[i-1])
        beta[i] = (F[i]-A[i]*beta[i-1])/(C[i]+A[i]*alpha[i-1])

result[n-1]=(F[n-1]-A[n-1]*beta[n-1])/(C[n-1]+A[n-1]*alpha[n-1])

for i in range(n-2,-1,-1):
    result[i]=alpha[i+1]*result[i+1]+beta[i+1]
