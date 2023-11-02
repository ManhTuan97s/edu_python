# Trình bày các bước của dự án Python
1. Tao folder du an
2. Tao file readme.md de viet doc cho du an
3. Cai dat python ban moi nhat
4. Tao moi truong ao: 
- để quản lý phiên bản python, tên và phiên bản site -packages
```commandline
python -m venv venv
``` 
4. Tạo file requirements.txt để lưu trữ thông tin tên và version của packages sử dụng trong dự án
5. Tạo file .ignore để liệt kệ ra những file hoặc folder kô muốn đẩy lên git repository
6. tạo file .env để lưu trữ các biến môi trường, thông tin nhạy cảm
7. Kích họat môi trường ảo (hoặc deactivate)
```commandline
./venv/Scripts/activate
```
8. Cài các gói đã khai báo trong file requirements.txt
```commandline
pip install -r requirements.txt
```
9. Gán môi trường ảo cho dự án (setup interpreter)
10. Cai dat cac extensions can thiet cho du an
11. Link doc https://doc.qt.io/qtforpython-5/quickstart.html
- tao ra 1 file .exe 
```commandline
python -m PyInstaller --onefile main.py
```

# Python basic
## Hằng số
- Quy tắc đặt tên hằng số
    + Không xuất phátt bằng chữ số 0-9
    + KHông được xuất phát bằng ký tự đặc biệt (!@#$%^&*)
    + Viết hoa toàn bộ tên hằng số, cách nhau bằng dấu _
    + Tên hằng và giá trị của hằng cách nhau TEN_HANG = 3.14
- Khai báo hằng số khi nào ?
    + Khi giá trị của hằng được dùng đi dùng lại trong chương trình

## Biến 
- Quy tắc đặt tên hằng số
    + Không xuất phátt bằng chữ số 0-9
    + KHông được xuất phát bằng ký tự đặc biệt (!@#$%^&*)
    + Viết thường toàn bộ tên biến, cách nhau bằng dấu _
    + Tên biến và giá trị của biếm cách nhau dấu " = " ten_bien = 50 
- Khai báo biến số khi nào ?
    + Khi cần lưu một giá trị biến đôir trong chương trình

## Kiểu dữ liệu
```python

"""
bien_dang_so_nguyen: tên biến
int: kiểu dữ liệu của biến là số nguyên
float: kiểu dữ liệu của biến là số thực
= gán giá trị
15: Giá trị của biến
"""
class CustomDataType:
    _id: int = 12
    _name: str = "Custom_data_type"
    
customDataCuaToi = CustomDataType(_id=17, _name="ten gi do")

bien_dang_so_nguyen: int = 15
bien_dang_so_thuc: float = 15.5
bien_dang_boolean: bool = 1 #True
bien_dang_boolean: bool = 0 #False
bien_dang_string: str = "day la string"
bien_dang_custom_data_type: CustomDataType = customDataCuaToi

```

- Dang du lieu list


## Buổi 3
```python
def di_dot_rung(cui, lua):
    print("da nhom cui")
    print("da cham lua")
    print("xong nhiem vu")
# hàm khởi tạo giá trị mặc định cho đối số
def tinh_tong(so_a=10, so_b=15):
    return so_a + so_b

#Khi mà chưa chắc chắn về số lượng đối số -> sử dụng *args
def tinh_tong(*args):
    # destrcuturing - lấy giá trị đối số đã truyền vào 
    tham_so_dau_tien = args[0]
    print(tham_so_dau_tien)


```
- ý nghĩa của hàm: định nghĩa một lần, sử dụng nhiều lần ở trong chương trình -> tránh lặp lại code
- Quy tac dat ten ham 
    + cú pháp con rắn (snake syntax)
    + các chữ cái viết thường cách nhau ký tự "_"
    + Không xuất phát bằng số và ký tự đặc biệt
    + nó nên là một động từ, hoặc cụm từ chỉ hanhf động 

- Đối số của hàm
    + cú pháp con rắn (snake syntax)
    + các chữ cái viết thường cách nhau ký tự "_"
    + Không xuất phát bằng số và ký tự đặc biệt
    + hàm có thể nhận nhiều đối số
    + đối số truyền vào có thể được gán giá trị mặc định
