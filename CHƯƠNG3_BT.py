#Câu 1
print("Chương trình kiểm tra năm nhuần")
year=int(input("Mời bạn nhập vào 1 năm: "))
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print("Năm ", year, " là năm nhuần")
else:
    print("Năm ", year, " không nhuần")

#Câu 2
print("Chương trình đếm số ngày trong tháng")
month=int(input("Nhập vào 1 tháng:"))
if month in (1,3,5,7,8,10,12):
    print("Tháng ", month, " có 31 ngày")
elif month in (4,6,9,11):
    print("Tháng ", month, " có 30 ngày")
elif month==2:
    year=int(input("Mời bạn nhập vào năm:"))
    if (year % 4 ==0 and year % 100 != 0) or year % 400==0:
        print("Tháng ",month, " có 29 ngày")
    else:
        print("Tháng ", month, " có 28 ngày")
else:
    print("Tháng ", month, " không hợp lệ")

#Câu 3
from math import sqrt
print("Chương trình Giải Phương trình bậc 2")
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
if a == 0:
 #bx+c=0
    if b == 0 and c ==0:
        print("Vô số nghiệm")
    elif b==0 and c !=0:
        print("Vô nghiệm")
    else:
        x=-c/b
        print("No x=",x)
else:
    delta=b**2-4*a*c
    if delta <0 :
        print("Vô No")
    elif delta ==0:
        x=-b/(2*a)
        print("No kép x1=x2=",x)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print("x1=",x1)
        print("x2=",x2)


#Câu 4
x, y, z = 3, 5, 7

print("a:", x == 3)
print("b:", x < y)
print("c:", x >= y)
print("d:", x <= y)
print("e:", x != y - 2)
print("f:", x < 10)
print("g:", x >= 0 and x < 10)
print("h:", x < 0 and x < 10)
print("i:", x >= 0 and x < 2)
print("j:", x < 0 or x < 10)
print("k:", x > 0 or x < 10)
print("l:", x < 0 or x > 10)


#Câu 5
#(a) i=5, j=5, k=7
#(b) i=3, j=5, k=5
#(c) i=7, j=3, k=7
#(d) i=5, j=3, k=3
#(e) i=5, j=3, k=5
#(f) i=7, j=7, k=3

#Câu 6
def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 0 or n > 99:
        return "Vui lòng nhập số từ 0 đến 99"

    if n == 0:
        return "không"
    elif n < 10:
        return don_vi[n]
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        elif n == 14:
            return "mười bốn"
        else:
            return "mười " + don_vi[n % 10]
    else:
        chuc = n // 10
        dv = n % 10

        hang_chuc = don_vi[chuc] + " mươi"

        if dv == 0:
            return hang_chuc
        elif dv == 1:
            return hang_chuc + " mốt"
        elif dv == 4:
            return hang_chuc + " tư"
        elif dv == 5:
            return hang_chuc + " lăm"
        else:
            return hang_chuc + " " + don_vi[dv]

# --- Nhập từ người dùng ---
try:
    n = int(input("Nhập số nguyên n (0 <= n <= 99): "))
    print("Cách đọc:", doc_so(n))
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")

#Câu 7
from datetime import datetime, timedelta

def ngay_ke_tiep(ngay, thang, nam):
    try:
        # Tạo đối tượng ngày
        ngay_hien_tai = datetime(nam, thang, ngay)
        
        # Ngày kế tiếp = ngày hiện tại + 1 ngày
        ngay_sau = ngay_hien_tai + timedelta(days=1)
        
        # Trả về định dạng dd/mm/yyyy
        return ngay_sau.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày nhập không hợp lệ."

# Nhập từ người dùng
try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    
    ket_qua = ngay_ke_tiep(ngay, thang, nam)
    print("Ngày kế tiếp là:", ket_qua)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ cho ngày, tháng, năm.")


#Câu 8

def tinh_toan(a, b, phep_toan):
    if phep_toan == '+':
        return a + b
    elif phep_toan == '-':
        return a - b
    elif phep_toan == '*':
        return a * b
    elif phep_toan == '/':
        if b == 0:
            return "Lỗi: Không thể chia cho 0"
        return a / b
    else:
        return "Lỗi: Phép toán không hợp lệ"

try:
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    phep_toan = input("Nhập phép toán (+, -, *, /): ")
    
    ket_qua = tinh_toan(a, b, phep_toan)
    print("Kết quả:", ket_qua)
except ValueError:
    print("Vui lòng nhập số hợp lệ.")

 #Câu 9
def xac_dinh_quy(thang):
    if 1 <= thang <= 3:
        return "Tháng {} thuộc Quý 1".format(thang)
    elif 4 <= thang <= 6:
        return "Tháng {} thuộc Quý 2".format(thang)
    elif 7 <= thang <= 9:
        return "Tháng {} thuộc Quý 3".format(thang)
    elif 10 <= thang <= 12:
        return "Tháng {} thuộc Quý 4".format(thang)
    else:
        return "Tháng không hợp lệ! Vui lòng nhập số từ 1 đến 12."

try:
    thang = int(input("Nhập tháng (1-12): "))
    print(xac_dinh_quy(thang))
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")

#Câu 10
x=int(input("Nhập x:"))
n=int(input("Nhập N:"))
s=0
for i in range(1,n+1):
 tu=x**i
 mau=1
 for j in range(1,i+1):
  mau=mau*j
  s=s+(tu/mau)
print("s({0},{1})={2}".format(x,n,s))

#Câu 11
while True:
    n=int(input("Nhập 1 số nguyên dương "))
    dem=0
    for i in range (1,n+1):
        if n % i ==0 :
            dem+=1
    if dem==2:
        print(n,"Là số nguyên tố")
    else:
        print(n,"Không là số nguyên tố")
    hoi=input("Tiếp không?(c/k):")
    if hoi is "k":
        break
print("BYE!")

#Câu 12

for i in range(1,11):
    for j in range(2,10):
        line="{0}*{1:>2}={2:>2}".format(j,i,i*j)
        print(line,end='\t')
    print()

#Câu 13
#Vô hạn dấu sao

#Câu 14
#In ra 2000 dấu sao

#Câu 15
#(a) range(5)
#→ Tạo dãy từ 0 đến 4.
#Kết quả: [0, 1, 2, 3, 4]

#(b) range(5, 10)
#→ Tạo dãy từ 5 đến 9.
#Kết quả: [5, 6, 7, 8, 9]

#(c) range(5, 20, 3)
#→ Tạo dãy từ 5 đến 19, bước nhảy 3.
#Kết quả: [5, 8, 11, 14, 17]

#(d) range(20, 5, -1)
#→ Tạo dãy từ 20 đến 6, bước nhảy -1.
#Kết quả: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

#(e) range(20, 5, -3)
#→ Tạo dãy từ 20 đến 8, bước nhảy -3.
#Kết quả: [20, 17, 14, 11, 8]

#(f) range(10, 5)
#→ Bước nhảy mặc định là +1. Nhưng 10 > 5 nên không thỏa điều kiện.
#Kết quả: [] (rỗng)

#(g) range(0)
#→ Dãy từ 0 đến -1 (không có số nào).
#Kết quả: []

#(h) range(10, 101, 10)
#→ Tạo dãy từ 10 đến 100, bước nhảy 10.
#Kết quả: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#(i) range(10, -1, -1)
#→ Tạo dãy từ 10 đến 0, bước nhảy -1.
#Kết quả: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#(j) range(-3, 4)
#→ Tạo dãy từ -3 đến 3.
#Kết quả: [-3, -2, -1, 0, 1, 2, 3]

#(k) range(0, 10, 1)
#→ Tạo dãy từ 0 đến 9, bước nhảy 1.
#Kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#Câu 16
#Có 16 dấu *

#Câu 17
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n =", n)

