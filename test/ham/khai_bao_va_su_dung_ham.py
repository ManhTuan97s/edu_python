def tinh_tong(*args):
    # destrcuturing - lấy giá trị đối số đã truyền vào 
    tham_so_dau_tien = args[0]
    print(tham_so_dau_tien)
    
# tinh_tong(13, "toi_la_tham_so_thu_2")

def tinh_ham_bac(*args):
    #tinh ham bac 2: ax^2 + bx +c =0
    if len(args) == 3:
        a= args[0]
        b= args[1]
        c= args[2]
        # dua 3 so a, b, c vao tinh toan phuong trinh bac 2
        
    #tinh ham bac 3: ax^3 + bx^2 +cx + d =0
    if len(args) == 4:
        a= args[0]
        b= args[1]
        c= args[2]
        d= args[3]
        # dua 3 so a, b, c,d vao tinh toan phuong trinh bac 3
        
tinh_ham_bac(2,3,5) # tinh ham bac 2

tinh_ham_bac(2,3,5,6) # tin ham bac 3

#hàm có trả về
def tinh_tong(a,b):
    kq= a+b
    return kq

tong=tinh_tong(4,5)
print("tong", tong)


def ham_nay_rat_kho():
    pass