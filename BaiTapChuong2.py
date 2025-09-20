#Câu 1
X = float(input("Nhập số tiền ban đầu: "))
lai_suat = 0.006  # 0,6%/tháng
so_thang = 18

# Sau mỗi 6 tháng cộng lãi vào gốc
for i in range(3):  # 18 tháng = 3 kỳ (mỗi kỳ 6 tháng)
    tien_lai = X * lai_suat * 6
    X += tien_lai

print("Tổng số tiền sau 18 tháng là:", round(X, 2))

#Câu 2
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = input("Nhập ký tự toán tử (+, -, *, /): ")

if c == '+':
    print("Kết quả:", a + b)
elif c == '-':
    print("Kết quả:", a - b)
elif c == '*':
    print("Kết quả:", a * b)
elif c == '/':
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: chia cho 0")
else:
    print("Ký tự không phải là toán tử hợp lệ")

 #Câu 3 
import math
r = float(input("Nhập bán kính hình tròn: "))
dien_tich = math.pi * r * r
print("Diện tích hình tròn là:", round(dien_tich, 2))

#Câu 4
thang = int(input("Nhập tháng (1-12): "))

if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", thang, "có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print("Tháng", thang, "có 30 ngày")
elif thang == 2:
    nam = int(input("Nhập năm: "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng 2 năm", nam, "có 29 ngày")
    else:
        print("Tháng 2 năm", nam, "có 28 ngày")
else:
    print("Tháng không hợp lệ")

#Câu 5

chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

n = int(input("Nhập số (0-99): "))

if n < 10:
    print(chu_so[n].capitalize())
elif n < 20:
    if n == 10:
        print("Mười")
    elif n == 15:
        print("Mười lăm")
    else:
        print("Mười " + chu_so[n % 10])
else:
    chuc = n // 10
    donvi = n % 10
    kq = chu_so[chuc].capitalize() + " mươi"
    if donvi == 1:
        kq += " mốt"
    elif donvi == 5:
        kq += " lăm"
    elif donvi != 0:
        kq += " " + chu_so[donvi]
    print(kq)

#Câu 6

import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm" if c != 0 else "Phương trình vô số nghiệm")
    else:
        print("Nghiệm: x =", -c / b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép: x =", -b / (2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Nghiệm x1 =", x1, ", x2 =", x2)

#Câu 7 
n = int(input("Nhập số nguyên n: "))
ket_qua = n + n**2 + n**3
print("Kết quả:", ket_qua)

#Câu 8
n = int(input("Nhập số n (1 < n < 9): "))
if 1 < n < 9:
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
else:
    print("n không hợp lệ")

#Câu 9 
n = int(input("Nhập n: "))

S = sum(range(1, n+1))
S1 = sum(2*i - 1 for i in range(1, n+1))
S2 = sum(2*i for i in range(1, n+1))
S3 = sum(i**2 for i in range(1, n+1))
S4 = sum(1/i for i in range(1, n+1))

print("S  =", S)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", round(S4, 4))

#Câu 10 
for i in range(1, 11):
    for j in range(2, 10):
        print(f"{j} x {i} = {j*i}", end="\t")
    print()
#Câu 11
import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(1, n+1):
    S += x**i / math.factorial(i)

print("S(x,n) =", round(S, 4))

#Câu 12 
n = int(input("Nhập số nguyên: "))
print("Số nhị phân:", bin(n)[2:])

#Câu 13 
import math
a = float(input("Nhập a (a ≠ 0): "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = b**2 - 4*a*c

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Nghiệm kép: x =", -b / (2*a))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Nghiệm: x1 =", x1, ", x2 =", x2)

#Câu 14
so_dem = 137
so_ngay = so_dem + 1   # ở 137 đêm → 138 ngày

thu_xuat_phat = 1  # Giả sử ngày đầu tiên là Thứ 2 (1 = Thứ 2, ..., 7 = CN)
thu_ve = (thu_xuat_phat + so_ngay - 1) % 7

ds_thu = ["Chủ Nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"]

print("Ngày về là:", ds_thu[thu_ve])

#Câu 15

# Nhập 3 số dương a, b, c cách nhau bởi dấu phẩy
a, b, c = map(float, input("Nhập 3 số dương a, b, c (cách nhau bởi dấu phẩy): ").split(","))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Có thể tạo thành một tam giác")
else:
    print("Không thể tạo thành một tam giác")

#Câu 16
day, month, year = map(int, input("Nhập ngày, tháng, năm: ").split(","))

import calendar
try:
    calendar.weekday(year, month, day)
    print("Ngày hợp lệ")
except:
    print("Ngày không hợp lệ")

#Câu 17
n = int(input("Nhập n: "))

# a) 1 + 2 + ... + 2n
tong_a = sum(range(1, 2*n+1))
print("a) =", tong_a)

# b) Tổng số lẻ < n
tong_b = sum(i for i in range(n) if i % 2 == 1)
print("b) =", tong_b)

# c) Tổng số chẵn < n
tong_c = sum(i for i in range(n) if i % 2 == 0)
print("c) =", tong_c)

#Câu 18
n = int(input("Nhập n: "))

# a) 1 + 1/2 + 1/3 + ... + 1/n
tong_a = sum(1/i for i in range(1, n+1))
print("a) =", tong_a)

# b) 2 + 4 + 6 + ... + n (n chẵn)
tong_b = sum(i for i in range(2, n+1, 2))
print("b) =", tong_b)

# c) 1^2 + 2^2 + 3^2 + ... + n^2
tong_c = sum(i**2 for i in range(1, n+1))
print("c) =", tong_c)

#Câu 19

# a) In tổng 1+2+...+n
def tong_n(n):
    print("Tổng =", sum(range(1, n+1)))

# b) Kiểm tra nguyên tố cùng nhau
import math
def nguyen_to_cung_nhau(m, n):
    if math.gcd(m, n) == 1:
        print("Hai số này là nguyên tố cùng nhau")
    else:
        print("Hai số này không nguyên tố cùng nhau")

# c) Chuyển giây thành giờ phút giây
def doi_giay(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    print(f"{h} giờ {m} phút {s} giây")

# d) Trả về |a-b|
def hieu_tuyet_doi(a, b):
    return abs(a-b)

# --- Test ---
tong_n(10)
nguyen_to_cung_nhau(15, 28)
doi_giay(3665)
print(hieu_tuyet_doi(5, 12))

#Câu 20 
import math

def f(m, n):
    ucln = math.gcd(m, n)
    for i in range(min(m, n), 1, -1):
        if m % i == 0 and n % i == 0 and i > 1:
            return i
    return 0

print(f(12, 18))
print(f(7, 13))