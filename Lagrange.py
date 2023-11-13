import math 
import numpy as np
import matplotlib.pyplot as plt

def mainFunc(x):
    # return 1 / (1 + 25 * x**2)
    return np.log(x+2)



def lagrangeFunc(x_i,i,n,x):
    l=1
    for k in range(n+1):
        if k!=i: 
            l*=(x-x_i[k])/(x_i[i]-x_i[k])
    return l

def polynomFunc(l_i,y_i,n):
    p=0
    for i in range(n+1):
        p+=y_i[i]*l_i[i]
    return p

def interpolationError(x):
    max=0
    max_point=0
    for i in range(len(x)):
        if abs(y_ip[i]-polynomFuncArray[i])>max:
            max=abs(y_ip[i]-polynomFuncArray[i])
            max_point = x_ip[i]
    return max, max_point




# ввід користувача
a = float(input("Введіть а: "))
b = float(input("Введіть b: "))

n = int(input("Введіть n: "))

x_z = float(input("Введіть x*: "))


h = (b-a)/(n)
nodes = []

#генерування вузлів
selectNodes = input ("Оберіть вузли\n1 - Рівномірні\n2 - Чебишева\n")

if selectNodes=='1':
    for i in range(n+1):
        x_i = a+i*h
        nodes.append(x_i)
if selectNodes=='2':
    for i in range(1,n+2):
        x_i = (a+b)/2+((b-a)/2)*math.cos(((2*i-1)*math.pi)/(2*(n+1)))
        nodes.append(x_i)



# генерування масиву у та функцій лагранжа
y_i = []
for i in range(n+1):
    y_i.append(mainFunc(nodes[i]))

l_i = []
for i in range(n+1):
    l_i.append(lagrangeFunc(nodes,i,n,x_z))

# поліном
result=polynomFunc(l_i,y_i,n)
print("Значення полінома в заданій точці = ",result,"\nЗначення похибки в цій точці = ", abs(mainFunc(x_z)-result))

# генерування графіків та точок 
n2=1000
if b-a>n2:
    n2=(b-a)+200
x_ip = np.linspace(a, b, n2)
y_ip = mainFunc(x_ip)
polynomFuncArray = []
for j in range(n2):
    l_ip=[]
    for i in range(n+1):
        l_ip.append(lagrangeFunc(nodes,i,n,x_ip[j]))
    polynomFuncArray.append(polynomFunc(l_ip,y_i,n))

#Визначення максимальної похибки
error, error_point=interpolationError(x_ip)
print("Максимальна похибка на відрізку = ",error, "\nВ точці: ", error_point)

#графік
pol, ax = plt.subplots()
ax.plot(x_ip, y_ip, label='функція', color='blue')

ax.plot(x_ip, polynomFuncArray, label='поліном', color='red')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

plt.show()







    


