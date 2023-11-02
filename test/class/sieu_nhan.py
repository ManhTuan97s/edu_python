



class SieuNhan():
    suc_manh: int = 50
    
    def __init__(self, mau_sac, so_luong_vu_khi):
        self._mau_sac = mau_sac
        self._so_luong_vu_khi = so_luong_vu_khi
        
    def thay_doi_suc_manh(self, suc_manh_moi):
        SieuNhan.suc_manh = suc_manh_moi
        
    def get_suc_manh(self):
        return SieuNhan.suc_manh
    
    @classmethod
    def get_suc_manh_cls(cls):
        return cls.suc_manh
        
# print(SieuNhan.suc_manh)

# # sieu_nhan_1=SieuNhan("do", 50)
# # print(sieu_nhan_1.get_suc_manh())

# print(SieuNhan.get_suc_manh_cls())

sieu_nhan_1=SieuNhan(mau_sac="do", so_luong_vu_khi=50)
sieu_nhan_2=SieuNhan(mau_sac="xanh", so_luong_vu_khi=15)
sieu_nhan_3=SieuNhan(mau_sac="vang", so_luong_vu_khi=10)

print(sieu_nhan_1.suc_manh)
print(sieu_nhan_2.suc_manh)

# lam the nao de sieu nhan 2 cap nhat suc manh cho ca gia dinh sieu 
sieu_nhan_2.thay_doi_suc_manh(40)
print("sieu_nhan_2.suc_manh", sieu_nhan_2.suc_manh)
print("sieu_nhan_1.suc_manh", sieu_nhan_1.suc_manh)



