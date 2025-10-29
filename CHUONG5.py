#Câu 1
def CheckDoiXung(s):
    flag=True
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            flag=False
            break
    return flag
def main():
    print("Nhập 1 chuỗi:")
    s=input()
    if(CheckDoiXung(s)):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")
while True:
    main()
    print("Tiếp không?(c/k):")
    s=input()
    if s=="k":
        break
print("CÁM ƠN BẠN")

#Câu 2
def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word=x
        if len(word.strip())!=0:
            s2=s2+word+" "
    return s2.strip()
s=" Trần Duy Thanh "
print(s,"=>",len(s))
s=ToiUuChuoi(s)
print(s,"=>",len(s))

#Câu 3
def CheckPrime(x):
     dem=0
     for i in range(1,x+1):
         if x % i ==0:
            dem+=1
     return dem==2
s="5;7;8;-2;8;11;-13;9;10"
arr=s.split(';')
sochan=0
soam=0
sont=0
sum=0
for x in arr:
    print(x)
    number=int(x)
    if number % 2 ==0:
        sochan+=1
    if number <0:
        soam+=1
    if CheckPrime(number):
        sont+=1
    sum=sum+number
print("Số chẵn =",sochan)
print("Số âm =",soam)
print("Số Nguyên tố =",sont)
print("Trung bình=",sum/len(arr))

#Câu 4
#Đổi chữ hoa / thường :upper(), lower(), capitalize(), title()              
#Xóa / thay thế       :strip(), replace()                                       
#Tìm kiếm             :find(), index(), count(), startswith(), endswith()
#Kiểm tra nội dung    :isalpha(), isdigit(), isalnum(), isspace()           
#Cắt và nối chuỗi     :split(), join(), slicing [start:end:step]             

#Câu 5
def xu_ly_chuoi(s):
    nguyen_am = "aeiouAEIOU"
    in_hoa = in_thuong = chu_so = ky_tu_dac_biet = khoang_trang = nguyen_am_count = phu_am = 0

    for ch in s:
        if ch.isupper():
            in_hoa += 1
        elif ch.islower():
            in_thuong += 1
        elif ch.isdigit():
            chu_so += 1
        elif ch.isspace():
            khoang_trang += 1
        else:
            ky_tu_dac_biet += 1

        if ch.isalpha():
            if ch in nguyen_am:
                nguyen_am_count += 1
            else:
                phu_am += 1

    print("Số chữ IN HOA:", in_hoa)
    print("Số chữ in thường:", in_thuong)
    print("Số chữ là chữ số:", chu_so)
    print("Số ký tự đặc biệt:", ky_tu_dac_biet)
    print("Số ký tự khoảng trắng:", khoang_trang)
    print("Số chữ nguyên âm:", nguyen_am_count)
    print("Số chữ phụ âm:", phu_am)

chuoi = input("Nhập vào 1 chuỗi bất kỳ: ")
xu_ly_chuoi(chuoi)

#Câu 6
import re

def NegativeNumberInStrings(s):
   
    numbers = re.findall(r'-\d+', s)
    if numbers:
        print("Các số nguyên âm trong chuỗi là:", ', '.join(numbers))
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

chuoi = input("Nhập chuỗi: ")
NegativeNumberInStrings(chuoi)

#Câu 7
def ToiUuChuoiDanhTu(s):

    tu = s.strip().split()

    tu_toi_uu = [t.capitalize() for t in tu]
    ket_qua = ' '.join(tu_toi_uu)
    
    return ket_qua

chuoi = input("Nhập chuỗi cần tối ưu: ")
ket_qua = ToiUuChuoiDanhTu(chuoi)
print("Chuỗi sau khi tối ưu:", ket_qua)

#Câu 8
import os

def lay_ten_file_day_du(duong_dan):
    return os.path.basename(duong_dan)

def lay_ten_file_khong_duoi(duong_dan):
    ten_day_du = os.path.basename(duong_dan)
    ten_khong_duoi, duoi = os.path.splitext(ten_day_du)
    return ten_khong_duoi

duong_dan = input("Nhập đường dẫn file nhạc: ")

print("Tên file có đuôi:", lay_ten_file_day_du(duong_dan))
print("Tên file không có đuôi:", lay_ten_file_khong_duoi(duong_dan))

