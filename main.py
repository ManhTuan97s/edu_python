# from custom_data_type import CustomDataType



# HANG_SO_PI = 3.14

# bien_so_nguyen = 45 
# print("bien_so_nguyen ban dau",bien_so_nguyen )
# bien_so_nguyen = 70
# print("bien_so_nguyen thay doi gia tri",bien_so_nguyen )

# bien_dang_so_nguyen: int = 15


###Buoi 2:
########################
####list
day_la_list_hoc_sinh =[] #list rong
print("type_day_la_list_hoc_sinh",type(day_la_list_hoc_sinh))
#[1, 2, 3, 4, 2424224]
day_la_list_so_nguyen =[1,2,3,3,3,3,4] # danh dau (index) tu so 0 -> truy xuat so 2 trong list nay
day_la_list_so_thuc =[
    1.667,
    2.4234,
    3.32424,
    4.23424  #->truy xuat so 4.23424 trong list nay
]
day_list_str = [
    "string 1",
    "text 2",
    "doan van 3"
]

day_la_list_du_lieu_ket_hop = [
    12,
    34.4324,
    "day la string",
    True, ## bool
    [
        "nguyen manh tuan",
        26,
        True,
        31.342, #->truy xuat so 31.342 trong list cua no
        {  # day la mot cai dict -> tuc la no duoc bao lai bang dau '{}'
            "name_card":"NGUYEN MANH TUAN",
            "card_number":532938423423424,
            "cvv": 232
        }
    ]
]

##truy xuat so 2 can lay trong list tren -> cong thuc la ten_bien_lits[gia_tri_index]
so_hai_can_lay = day_la_list_so_nguyen[1]
print("so_hai_can_lay",so_hai_can_lay)

###->truy xuat so 4.23424 trong list nay
so_thuc_can_lay = day_la_list_so_thuc[3]
print("so_thuc_can_lay",so_thuc_can_lay)

#->truy xuat so 31.342 trong list cua no
so_31_342_can_lay = day_la_list_du_lieu_ket_hop[4][3]
print("so_31_342_can_lay",so_31_342_can_lay)


#########################
######dict -> viet tat cua tu dien dictionary
day_la_mot_cai_dict = {
    "key_1": 23,
    "key_2": "value 2" # truy xuat gia tri phan tu co ky la "key_2" trong dict "day_la_mot_cai_dict"
}

day_la_dict_co_du_lieu_ket_hop ={
    "ho": "Nguyen",
    "ten": "Tuan",
    "sdt": 884512121,
    "so_luong_ny": 5,
    "list_ten_ny": ["Hong", "Hanh", "Nga", "mit","xoai"],
    "dict_card_info": {
        "name_card":"NGUYEN MANH TUAN",
        "card_number":532938423423424, #lay_card_number tu day_la_dict_co_du_lieu_ket_hop
        "cvv": 232
    }
    
}

# truy xuat gia tri phan tu co ky la "key_2" trong dict "day_la_mot_cai_dict"
phan_tu_co_key_2 = day_la_mot_cai_dict["key_2"]
print("phan_tu_co_key_2",phan_tu_co_key_2)
#lay_card_number tu day_la_dict_co_du_lieu_ket_hop
card_info_muon_lay = day_la_dict_co_du_lieu_ket_hop["dict_card_info"]["card_number"]
print("card_info_muon_lay",card_info_muon_lay)

dict_card_info = day_la_dict_co_du_lieu_ket_hop["dict_card_info"]
print("dict_card_info",dict_card_info) #{'name_card': 'NGUYEN MANH TUAN', 'card_number': 532938423423424, 'cvv': 232}

dict_card_info = day_la_dict_co_du_lieu_ket_hop.get("dict_card_infoooooooo") #-> tra ve None va khong co loi
print("dict_card_info",dict_card_info) 
"""
    Luu y:
        - Khi chúng ta khẳng định rằng dict đó luôn có key đó thì mới dùng kiểu truy xuất ten_dict["ten_key"]
        - Ngược lại nếu chưa chắc chắn thì dùng .get("ten_key")-> bởi vì dùng get thì nếu không có key thì app trả về None và không báo lỗi

"""
# dict_card_info = day_la_dict_co_du_lieu_ket_hop["dict_card_info0999999999"] ### Loi 
# print("dict_card_info",dict_card_info) 

if day_la_dict_co_du_lieu_ket_hop.get("dict_card_info0999999999") != None:
    dict_card_info999999999 = day_la_dict_co_du_lieu_ket_hop.get("dict_card_info0999999999")
    

try:
    day_la_dict_co_du_lieu_ket_hop["dict_card_info0999999999"]
except Exception as error:
    import traceback
    traceback.print_exc()
    print(error)
    
try:
    34/0
except ZeroDivisionError as e:
    print("loi chia cho khong")
except Exception as e:
    import traceback
    traceback.print_exc()
    
######su dung cac method cua list
day_la_list_so_nguyen.append(2424224)
# print('day_la_list_so_nguyen sau khi append them phan tu', day_la_list_so_nguyen)

hung_list_copy = day_la_list_so_nguyen.copy()
# print('hung_list_copy', hung_list_copy)
# print('list_cu', day_la_list_so_nguyen)
print('Dem so 3 list', day_la_list_so_nguyen.count(3))
print('Vi tri tim thay so 3 dau tien trong list', day_la_list_so_nguyen.index(3))


# day_la_list_so_nguyen.clear()
# print('day_la_list_so_nguyen sau khi clear', day_la_list_so_nguyen)


######su dung cac method cua list
######su dung cac method cua dict
######cac method cua Python String Method
###### cac method cua Python Math Method
####### Numpy
##### Pandas python

########### Buổi 3
##### Hàm, Class, OOP(object orientation programming)

##### 1.Hàm
"""Khai bao ham (hoac dinh nghia ham, khoi tao ham)
- def: la namespace cua python, su dung khi dinh nghia ham
- day_la_ten_ham: ten ham
- (): noi truyen vao doi so cua ham, muon lam gi thi them doi so tuong ung
def day_la_ten_ham(doi_so_1, doi_so_2):
    print("Day la noi dung cua ham")

"""

def day_la_ten_ham(doi_so_1, doi_so_2):
    print("Day la noi dung cua ham")
    
def di_dot_rung(cui, lua):
    print("da nhom cui")
    print("da cham lua")
    print("xong nhiem vu")
    
def tinh_tong(*args):
    # destrcuturing - lấy giá trị đối số đã truyền vào 
    tham_so_dau_tien = args[0]
    print(tham_so_dau_tien)
    
tinh_tong(13, "toi_la_tham_so_thu_2")

# tham so *args
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

#tham so **args
def tinh_ham_bac(**args):
    #tinh ham bac 2: ax^2 + bx +c =0
    if len(args) == 3:
        a= args["a"]
        b= args["b"]
        c= args["c"]
        # dua 3 so a, b, c vao tinh toan phuong trinh bac 2
        
    #tinh ham bac 3: ax^3 + bx^2 +cx + d =0
    if len(args) == 4:
        a= args["a"]
        b= args["b"]
        c= args["c"]
        d= args["d"]
        # dua 3 so a, b, c,d vao tinh toan phuong trinh bac 3
 
 # su dung ham       
tinh_ham_bac(a=2,b=3,c=5) # tinh ham bac 2
 # su dung ham  
tinh_ham_bac(a=2,b=3,c=5,d=6) # tin ham bac 3

#hàm không có trả về
def in_ra_cai_gi_do():
    print("da in xong")

in_ra_cai_gi_do()

#hàm có trả về
def tinh_tong(a,b):
    kq= a+b
    return kq


tong=tinh_tong(4,5)
print("tong", tong)

# Khi ham chua co noi dung thi dua vao pass o than ham de tranh loi
def ham_nay_rat_kho():
    pass

### Hàm mặc danh lambda -> anonimous funtion
x = lambda a: a + 10
print(x(5)) #-> 15

def tinh_bieu_thuc(a):
	return a+10
print(tinh_bieu_thuc(5)) #-> 15


## 2. CLASS

class TenClass(TenClassKeThua):
    _thuoc_tinh_class: int = 18
    
    def __init__(self, tham_so_1, tham_so_2, *args): #ham construct, noi khoi tao cac gia tri truyen vao cho class
        self._tham_so_1 = tham_so_1
        self._tham_so_2 = tham_so_2
        self._tham_so_3 = args[0]
        
    def day_la_phuong_thuc_cua_class(self):
        pass
    
    def in_ra_tham_so_1(self):
        print(self._tham_so_1)
        
    def tra_ve_tong_tham_so_1_va_tham_so_2(self):
        return self._tham_so_1 + self._tham_so_2
    
    def tinh_tong_ket_hop_tham_so_ngoai_truyen_vao(self, tham_so_ngoai):
        return self._tham_so_1 + self._tham_so_2 + tham_so_ngoai
    
    @classmethod
    def thuoc_tinh_class(cls):
        return cls._thuoc_tinh_class
    
    def tra_ve_gia_tri_thuoc_tinh_class(self):
        return self._thuoc_tinh_class
    
# y nghia cua classmethod
TenClass.thuoc_tinh_class

my_class = TenClass()
#my_class co day du thuoc tinh va phuong thuc cua class
my_class.tra_ve_gia_tri_thuoc_tinh_class()










