
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import textwrap
#https://www.stat.ee/pressiteade-2019-111
#https://www.stat.ee/pressiteade-2019-104

fail=open("text_num.txt","r",encoding="utf-8-sig")
nazvanie=[]#название
znachenie=[]#значения
for line in fail:
    n=line.find(",")
    nazvanie.append(line[0:n].strip())
    znachenie.append(float(line[n+1:len(line)].strip()))
fail.close()
print(nazvanie)
print(znachenie)

plt.bar(nazvanie,znachenie)
plt.xticks(nazvanie, wrap=True, rotation=30, ha="right", va="top")
plt.yticks(range(0,101,5))
plt.grid(True,alpha=0.5,linestyle='--')
plt.title('IKT turvameetodite kasutamine ettevõttes 2018')
plt.ylabel('Ettevõttete osakaal %')
#plt.xlabel('') тут без названия всё понятно
plt.subplots_adjust(left=0.125, bottom=0.3, right=0.9, top=0.88, wspace=0.2, hspace=0.2)
plt.show()

#----------------------------------------------
x1 = np.linspace(-9,-1,100)
y1 = -(1/8)*(x1+9)**2+8
x2 = np.linspace(1,9,100)
y2 = -(1/8)*(x2-9)**2+8
x3 = np.linspace(-9,-8,100)
y3 = 7*(x3+8)**2+1
x4 = np.linspace(8,9,100)
y4 = 7*(x4-8)**2+1
x5 = np.linspace(-8,-1,100)
y5 = (1/49)*(x5+1)**2
x6 = np.linspace(1,8,100)
y6 = (1/49)*(x6-1)**2
x7 = np.linspace(-8,-1,100)
y7 = -(4/49)*(x7+1)**2
x8 = np.linspace(1,8,100)
y8 = -(4/49)*(x8-1)**2
x9 = np.linspace(-8,-2,100)
y9 = (1/3)*(x9+5)**2-7
x10 = np.linspace(2,8,100)
y10 = (1/3)*(x10-5)**2-7
x11 = np.linspace(-2,-1,100)
y11 = -(2)*(x11+1)**2-2
x12 = np.linspace(1,2,100)
y12 = -(2)*(x12-1)**2-2
x13 = np.linspace(-1,1,100)
y13 = -(4)*x13**2+2
x14 = np.linspace(-1,1,100)
y14 = 4*x14**2-6
x15 = np.linspace(-2,0,100)
y15 = -(1.5)*x15+2
x16 = np.linspace(0,2,100)
y16 = 1.5*x16+2
print(x1)
print(y1)

plt.subplots()
plt.title("Бабочка")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")

plt.grid(True)# Отображение сетки на координатной плоскости
plt.plot(x1,y1 ,'-b',linewidth=5,label="Ряд 1")
plt.plot(x2,y2 ,'-b',linewidth=5,label="Ряд 2")
plt.plot(x3,y3 ,'-b',linewidth=5,label="Ряд 3")
plt.plot(x4,y4 ,'-b',linewidth=5,label="Ряд 4")
plt.plot(x5,y5 ,'-b',linewidth=5,label="Ряд 5")
plt.plot(x6,y6 ,'-b',linewidth=5,label="Ряд 6")
plt.plot(x7,y7 ,'-b',linewidth=5,label="Ряд 7")
plt.plot(x8,y8 ,'-b',linewidth=5,label="Ряд 8")
plt.plot(x9,y9 ,'-b',linewidth=5,label="Ряд 9")
plt.plot(x10,y10 ,'-b',linewidth=5,label="Ряд 10")
plt.plot(x11,y11 ,'-b',linewidth=5,label="Ряд 11")
plt.plot(x12,y12 ,'-b',linewidth=5,label="Ряд 12")
plt.plot(x13,y13,'-b',linewidth=5,label="Ряд 13")
plt.plot(x14,y14 ,'-b',linewidth=5,label="Ряд 14")
plt.plot(x15,y15 ,'-b',linewidth=5,label="Ряд 15")
plt.plot(x16,y16 ,'-b',linewidth=5,label="Ряд 16")
plt.legend()
plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран

