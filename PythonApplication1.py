#Cau 4
print("Chao cac ban!")
#Cau 5
print("Nguyen Thi Nhu Y")
#Cau 6
print("""Minh ve minh co nho ta
Minh lam nam ay thiet tha man nong
Minh ve minh co nho khong?
Nhin cay nho nui nhin song nho nguon""")
#Cau 7
s = input("Nhap chuoi: ")
print("Chuoi vua nhap: ",s)
#Cau 8
print("****")
print(" *  *")
print("  *  *")
print("   ****")
#Cau 9
stars = [9, 9, 9, 9]

width = max(stars)

for s in stars:
    print(" " * ((width - s) // 2) + "*" * s)
#Cau 10
stars = [1, 3, 7, 3, 5, 11, 2, 2]

width = max(stars)

for s in stars:
    print(" " * ((width - s) // 2) + "*" * s)
