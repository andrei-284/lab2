import requests
import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt
#Выгрузка данных
url = 'https://jenyay.net/uploads/Student/Modelling/task_02.txt'
r = requests.get(url, allow_redirects=True)
f = open("data_02.txt", "w")
f.write(r.text)
f.close()
f = open("data_02.txt", "r")
i=1
for line in f:
    if i==17:
        string=line
        print(line)
    i=i+1
f.close()
ar_of_str=string.split(';')
ar_of_num[2]=(ar_of_num[2]).replace('\n','')
#Переменные
D=float(ar_of_num[0])
r=D/2
fmin=float(ar_of_num[1])
fmax=float(ar_of_num[2])
c=3*(10**8)
#Функция для расчета
def h(n,x):
    return sp.spherical_jn(n,x)+1j*sp.spherical_yn(n,x)
def bn(n,x):
    return (x*sp.spherical_jn(n-1,x)-n*sp.spherical_jn(n,x))/(x*h(n-1,x)-n*h(n,x))
def an(n,x):
    return sp.spherical_jn(n,x)/h(n,x)
def epr(f,Nmax):
    l=c/f
    k=2*np.pi/l
    epr_val=0
    for i in range(1,Nmax):
        epr_val=epr_val+(-1)**i*(i+1/2)*(bn(i,k*r)-an(i,k*r))
    epr_val=np.power(np.abs(epr_val),2)
    return epr_val*(l**2)/np.pi
#Расчет
f_list=np.linspace(fmin,fmax,num=100)
epr_list=[epr(i,10) for i in f_list]
epr_plot=[i/(np.pi*r**2) for i in epr_list]
x_plot=[2*np.pi*r/(c/i) for i in f_list]
#График
plt.figure(figsize=(12,6))
plt.plot(x_plot,epr_plot)
plt.title('ЭПР')
plt.xlabel(r'$\frac{2\pi r}{\lambda}$')
plt.ylabel(r'$\frac{\sigma}{\pi r^2}$')
plt.grid(True)
plt.show()
#Вывод в файл
with open("output.txt", "w") as txt_file:
    for line in zip(f_list,epr_list):
        txt_file.write("{:10.6f}{:10.06f} \n".format(line[0],line[1]))
