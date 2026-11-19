# Quản lý thẻ bệnh nhân bằng Python Console

## Đề bài

Một phòng khám tư nhân cần công cụ chạy trên Console Python để lễ tân nhập nhanh thông tin bệnh nhân khi đến khám và hiển thị lại dưới dạng **thẻ bệnh nhân**. Chương trình cần:

- Nhập từ bàn phím: tên, giới tính, năm sinh, số điện thoại, email, triệu chứng ban đầu, chi phí khám.
- Ép kiểu: **năm sinh → `int`**, **chi phí khám → `float`**, các trường còn lại giữ `str`.
- Tự sinh mã bệnh nhân theo định dạng **`BN` + năm sinh + 3 số ngẫu nhiên** (ví dụ `BN1998456`), không trùng trong một lần chạy.
- Kiểm tra kiểu dữ liệu từng trường bằng `type()` và hiển thị cho người dùng.
- In thẻ bệnh nhân rõ ràng, dễ đọc.

## Phân tích

| Yêu cầu | Cách xử lý |
|---|---|
| Nhập dữ liệu | `input()` luôn trả về chuỗi, dùng thêm `.strip()` để bỏ khoảng trắng thừa ở đầu/cuối |
| Ép kiểu | `int(birth_year)` để năm sinh dùng được như số; `float(cost)` vì chi phí có thể có phần lẻ |
| Mã bệnh nhân | `random.randint(100, 999)` luôn cho đúng 3 chữ số; ghép bằng f-string `f"BN{birth_year}{random_part}"` |
| Mã duy nhất | Lưu các mã đã cấp vào một `set`; nếu sinh trùng thì sinh lại |
| Kiểm tra kiểu | `type(value).__name__` trả về tên kiểu (`str`, `int`, `float`) để in ra |
| Thẻ bệnh nhân | f-string căn lề trái `{label:<11}` để dấu `:` thẳng cột |

> Lưu ý: số điện thoại giữ kiểu `str` chứ không ép sang `int`, vì ép sang số sẽ làm mất số `0` ở đầu (`0394556888` → `394556888`).

## Lời giải

File: [`the_benh_nhan.py`](the_benh_nhan.py)

### 1. Nhập thông tin

```python
name = input("Nhập tên bệnh nhân: ").strip()
gender = input("Nhập giới tính: ").strip()
birth_year = input("Nhập năm sinh: ").strip()
phone = input("Nhập số điện thoại: ").strip()
email = input("Nhập email: ").strip()
symptom = input("Nhập triệu chứng ban đầu: ").strip()
cost = input("Nhập chi phí khám: ").strip()
```

### 2. Ép kiểu dữ liệu

```python
birth_year = int(birth_year)
cost = float(cost)
```

### 3. Tạo mã bệnh nhân tự động

```python
used_ids = set()

def generate_patient_id(birth_year):
    while True:
        random_part = random.randint(100, 999)
        patient_id = f"BN{birth_year}{random_part}"
        if patient_id not in used_ids:
            used_ids.add(patient_id)
            return patient_id
```

### 4 + 5. Kiểm tra kiểu và hiển thị thẻ

```python
def show_field(label, value, suffix=""):
    print(f"{label:<11}: {value}{suffix} ({type(value).__name__})")

print("\n--- THẺ BỆNH NHÂN ---")
print(f"{'Mã BN':<11}: {patient_id}")
print()
show_field("Tên", name)
show_field("Giới tính", gender)
show_field("Năm sinh", birth_year)
show_field("Điện thoại", phone)
show_field("Email", email)
show_field("Triệu chứng", symptom)
show_field("Chi phí", cost, " VND")
```

## Cách chạy

```bash
python the_benh_nhan.py
```

## Kết quả

```
Nhập tên bệnh nhân: Nguyễn Thiết Lang
Nhập giới tính: Nam
Nhập năm sinh: 1998
Nhập số điện thoại: 0394556888
Nhập email: thietlang@gmail.com
Nhập triệu chứng ban đầu: Đau đầu
Nhập chi phí khám: 250000

--- THẺ BỆNH NHÂN ---
Mã BN      : BN1998875

Tên        : Nguyễn Thiết Lang (str)
Giới tính  : Nam (str)
Năm sinh   : 1998 (int)
Điện thoại : 0394556888 (str)
Email      : thietlang@gmail.com (str)
Triệu chứng: Đau đầu (str)
Chi phí    : 250000.0 VND (float)
```

3 số cuối của mã bệnh nhân là ngẫu nhiên nên mỗi lần chạy sẽ khác nhau.
