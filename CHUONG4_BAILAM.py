#Câu 1
from math import sqrt
print("Chương trình tính diện tích Tam Giác")
a=float(input("Nhập cạnh a>0:"))
b=float(input("Nhập cạnh b>0:"))
c=float(input("Nhập cạnh c>0:"))
if (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a:
    print("Tam giác không hợp lệ")
else:
    cv=a+b+c
    p=cv/2
    dt=sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích =",dt)

#Câu 2
from random import randrange
while True:
    somay=randrange(1,101)
    solandoan=0
    win=False
    while solandoan<7:
          solandoan+=1
          songuoi=int(input("Máy đoán [1..100], mời bạn đoán:"))
          print("Bạn đoán lần thứ ",solandoan)
          if somay==songuoi:
                print("Chúc mừng bạn đoán đúng, số máy là=",somay)
                win=True
                break
          if somay>songuoi:
                print("Bạn đoán sai, số máy > số bạn")
          elif somay<songuoi:
                print("Bạn đoán sai, số máy < số bạn")
    if win==False:
          print("GAME OVER!, số máy =",somay)
    hoi=input("Tiếp không?")
    if hoi=="k":
          break
print("Cám ơn bạn đã chơi Game!")

#Câu 3
def BMI(height,weight):
    return weight/(height**2)
def PhanLoai(bmi):
    if bmi<18.5:
        return "Gầy"
    elif bmi<=24.9:
        return "Bình thường"
    elif bmi<=29.9:
        return "Hơi Béo"
    elif bmi<=34.9:
        return "Béo Phì Cấp Độ 1"
    elif bmi<=39.9:
        return "Béo Phì Cấp Độ 2"
    else:
        return "Béo Phì Cấp độ 3"
def NguyCoBenh(bmi):
    if bmi<18.5:
        return "Thấp"
    elif bmi<=24.9:
        return "Trung Bình"
    elif bmi<=29.9:
        return "Cao"
    elif bmi<=34.9:
        return "Cao"
    elif bmi<=39.9:
        return "Rất cao"
    else:
        return "Nguy Hiểm"
print("Nhập vào chiều cao:")
height=float(input())
print("Nhập vào cân nặng:")
weight=float(input())
bmi=BMI(height,weight)
print("BMI của bạn=",bmi)
print("Phân loại bạn=",PhanLoai(bmi))
print("Nguy cơ bệnh của Bạn=",NguyCoBenh(bmi))

#Câu 4
def ROI(dt,cp):
    return (dt-cp)/cp
def GoiYDauTu(roi):
    if roi>=0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
print("Chương trình tính ROI")
dt=int(input("Nhập Doanh Thu:"))
cp=int(input("Nhập chi phí:"))
roi=ROI(dt,cp)
print("Tỉ Lệ ROI=",roi)
print("==>",GoiYDauTu(roi))

#Câu 5
def fibonacci(n):
    if n<=2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
def listfibo(n):
    for i in range(1,n+1):
        print(fibonacci(i),end='\t')
print(fibonacci(9))
listfibo(9)

#Câu 6
import random

start, stop = 0, 100
values = [4.5, 34, -1, 100, 0, 99]
print(f"Các giá trị có thể xuất hiện trong randrange({start}, {stop}):")
for v in values:
    if isinstance(v, int) and start <= v < stop:
        print(f"{v} Có thể xuất hiện")
    else:
        print(f"{v} Không thể xuất hiện")


#Câu 7
import math
xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))
xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))

AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Độ dài đoạn AB là:", round(AB, 2))

#Câu 8
import math
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x:.4f}")
else:
    print("Giá trị không hợp lệ! Yêu cầu: a > 0, a ≠ 1, x > 0.")

#Câu 9
import math
n = int(input("Nhập số lượng lớp căn: "))

values = []
for i in range(n):
    x = float(input(f"Nhập giá trị thứ {i+1}: "))
    values.append(x)

res = math.sqrt(values[-1])
for i in range(n - 2, -1, -1):
    res = math.sqrt(values[i] + res)

print("Giá trị căn lồng nhau là:", round(res, 4))


#Câu 10
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hinh1():
    print("      *      ")
    print("      * *    ")
    print("      * * *  ")
    print("* * * * * * *")
    print("* * *        ")
    print("* *          ")
    print("*            ")

def hinh2():
    print("      *      ")
    print("      * *    ")
    print("      *   *  ")
    print("* * * * * * *")
    print("*   *        ")
    print("* *          ")
    print("*            ")

def hinh3():
    print("      * * * *")
    print("      * * *  ")
    print("      * *    ")
    print("      *      ")
    print("    * *      ")
    print("  * * *      ")
    print("* * * *      ")

def hinh4():
    print("      * * * *")
    print("      *   *  ")
    print("      * *    ")
    print("      *      ")
    print("    * *      ")
    print("  *   *      ")
    print("* * * *      ")

clear()
print("Hình 1:")
hinh1()
time.sleep(5)

clear()
print("Hình 2:")
hinh2()
time.sleep(5)

clear()
print("Hình 3:")
hinh3()
time.sleep(5)

clear()
print("Hình 4:")
hinh4()

#Câu 11
#Trường hợp 1
#5
#5
#0

#Trường hợp 2
#5
#5
#5

#Trường hợp 3
#5
#5
#0

#Câu 12
def oscillate():
    for i in range(-3, 5):  # từ -3 đến 4
        if i < 0:
            print(i, abs(i), end=" ")
        elif i == 0:
            print(0, 0, end=" ")
        else:
            print(i, -i, end=" ")

oscillate()

#Câu 13
def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_so_hoan_thien(n):
    return tong_uoc(n) == n

def la_so_thinh_vuong(n):
    return tong_uoc(n) > n

n = int(input("Nhập số nguyên dương n: "))

if la_so_hoan_thien(n):
    print(n, "là số hoàn thiện.")
elif la_so_thinh_vuong(n):
    print(n, "là số thịnh vượng.")
else:
    print(n, "không phải là số hoàn thiện hoặc số thịnh vượng.")

