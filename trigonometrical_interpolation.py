import math 
import numpy as np
import matplotlib.pyplot as plt

def mainFunc(x):
    # return pow(np.exp(1),np.sin(x)+np.cos(x))
    return 3*np.cos(15*x)

def koef(a_k,b_k,nodes,n,isOdd):
    for i in range(0,n+1):
        s=0
        if isOdd==True:
            for j in range(0,2*n+1):
                s+=mainFunc(nodes[j])*math.cos((2*math.pi*j*i)/(2*n+1))
            a_k.append((2/(2*n+1))*s)
            if i!=n:
                s=0
                k=i+1
                for j in range(0,2*n+1):
                    s+=mainFunc(nodes[j])*math.sin((2*math.pi*j*k)/(2*n+1))
                b_k.append((2/(2*n+1))*s)
        else:
            for j in range(0,2*n):
                s+=mainFunc(nodes[j])*math.cos((math.pi*j*i)/(n))
            a_k.append(1/(n)*s)
            if i<n-1:
                s=0
                k=i+1
                for j in range(0,2*n):
                    s+=mainFunc(nodes[j])*math.sin((math.pi*j*k)/(n))
                b_k.append((1/n)*s)
            
def polynom(a_k,b_k,n,isOdd,t):
    q=a_k[0]/2
    sum=0
    if isOdd==True:
        fin=n
    else:
        fin=n-1
    for i in range(0,fin):
        sum+=a_k[i+1]*np.cos((i+1)*t)
        # print(t,np.cos((i+1)*t))
    for i in range(0,fin):
        sum+=b_k[i]*np.sin((i+1)*t)
    q+=sum
    if isOdd!=True:
        q+=a_k[n]/2*np.cos((n)*t)
    return q

def interpolationError(x):
    max=0
    max_point=0
    for i in range(len(x)):
        if abs(y_ip[i]-polynomFuncArray[i])>max:
            max=abs(y_ip[i]-polynomFuncArray[i])
            max_point = x_ip[i]
    return max, max_point

            
nodes_n=int(input("Кількість вузлів інтерполяції: "))
nodes = [0 + i*((2*math.pi)/(nodes_n)) for i in range(nodes_n)]
n=0
a_k=[]
b_k=[]
isOdd=False

if nodes_n%2==0:
    n=int(nodes_n/2)
else:
    n=int((nodes_n-1)/2)
    isOdd=True

y_i = []
for i in range(nodes_n):
    y_i.append(mainFunc(nodes[i]))

koef(a_k,b_k,nodes,n,isOdd)


x_ip = np.linspace(0, 2*math.pi, 1000)
y_ip = mainFunc(x_ip)
polynomFuncArray = []
for i in range(len(x_ip)):
    polynomFuncArray.append(polynom(a_k,b_k,n,isOdd,x_ip[i]))

error, error_point=interpolationError(x_ip)
print("Максимальна похибка на відрізку = ",error, "\nВ точці: ", error_point)


for i in range(len(a_k)):
    print(i,"   ", a_k[i])

print("Коефіцієнти b_k: ", b_k)
# print(nodes)
# print(mainFunc(nodes))
# for i in range(len(nodes)):
# print(polynom(a_k,b_k,n,isOdd,(2*np.pi)/(2)))



pol, ax = plt.subplots()
for i in range(len(nodes)):
    ax.scatter(nodes[i], mainFunc(nodes[i]))
ax.plot(x_ip, polynomFuncArray, label='поліном', color='red', linewidth=3)
ax.plot(x_ip, y_ip, label='функція', color='blue')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# import functions as funcs
# a = 0
# b = 2*np.pi
# number_nodes = 7
# degree = number_nodes//2
# nodes = [a + i*((b-a)/number_nodes) for i in range(number_nodes)]
# print(nodes)
# func_values = [funcs.func(nodes[i]) for i in range(number_nodes)]
# a_k = [sum([func_values[j] * np.cos( (2*np.pi*j*i) / (number_nodes) ) for j in range(number_nodes)]) * (2.0/number_nodes) for i in range(degree + 1)]
# b_k = [sum([func_values[j] * np.sin( (2*np.pi*j*i) / (number_nodes) ) for j in range(1,number_nodes)]) * (2.0/number_nodes) for i in range(1,degree + 1)]
# if (number_nodes%2 == 0):
#   b_k.pop()
# test = [funcs.interpolation_value(nodes[i],a_k,b_k,number_nodes) for i in range(number_nodes)]
# x = np.linspace(a,b,1000)
# y = [funcs.func(item) for item in x]
# y_interpolation = [funcs.interpolation_value(item,a_k,b_k,number_nodes) for item in x]
# (deviation, x_deviation) = (0,0)
# for i in range(len(x)):
#   curr_deviation = np.abs(y[i] - y_interpolation[i])
#   if (curr_deviation > deviation):
#     (deviation,x_deviation) = (curr_deviation, x[i])

# ## prints
# print("a_k and b_k")
# print(" | ".join([str(round(item,4)) for item in a_k]))
# print(" | ".join([str(round(item,4)) for item in b_k]))
# print("Check or values are equal")
# print(" | ".join([str(round(item,4)) for item in func_values]))
# print(" | ".join([str(round(item,4)) for item in test]))
# print(f"Max deviation and point x: {deviation} | {x_deviation}")

# ## plot
# plt.figure(figsize=(10,6))
# plt.plot(x, y, label='f(x)', linewidth=2)
# plt.plot(x, y_interpolation, label='interpolation', linestyle='dashed', linewidth=2)
# plt.scatter(nodes,func_values)
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Trigonometric Interpolation')
# plt.grid(True)
# plt.show()
