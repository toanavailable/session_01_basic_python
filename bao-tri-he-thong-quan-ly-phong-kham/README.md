# Bảo trì hệ thống quản lý phòng khám - Sửa lỗi kiểu dữ liệu cân nặng

## Đề bài

Điều dưỡng dùng phần mềm để nhập chỉ số của bệnh nhân. Cân nặng phải được lưu dưới dạng **số thực (`float`)** để sau này tính BMI và các chỉ số y khoa khác.

Sự cố hiện tại: cân nặng vẫn hiển thị đúng (`65.5`) nhưng khi kiểm tra kiểu lại ra `<class 'str'>`. Nếu không sửa, các phép tính như BMI sẽ không thực hiện được.

Yêu cầu: (1) dò luồng thực thi và phân tích lỗi; (2) sửa lại bằng ép kiểu (type casting) để `print(type(weight))` trả về `<class 'float'>`.

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py)

```python
print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")
weight = input("Nhập cân nặng bệnh nhân : ")

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : " , name_patient)
print("Cân nặng đã nhập : " , weight)

# Trưởng nhóm IT viết thêm dòng này để kiểm tra dữ liệu của cân nặng
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : " , type(weight))
```

## (1) Phân tích lỗi

### Dò luồng thực thi (trace code)

Với dữ liệu nhập `Nguyễn Văn A` và `65.5`:

| Dòng | Câu lệnh | Trạng thái / kết quả |
|---|---|---|
| 2 | `name_patient = input(...)` | `name_patient = "Nguyễn Văn A"` (str) ✅ |
| 3 | `weight = input(...)` | `weight = "65.5"` (**str**) ❌ không phải số `65.5` |
| 7 | `print("Cân nặng đã nhập : ", weight)` | In ra `65.5`. Nhìn thì đúng vì `print()` không hiện dấu nháy của chuỗi |
| 10 | `print(..., type(weight))` | In ra `<class 'str'>`, lộ ra lỗi |

### Đặc điểm của hàm `input()`

- `input()` dừng chương trình, chờ người dùng gõ và nhấn Enter.
- Giá trị trả về **luôn là chuỗi (`str`)**, dù người dùng gõ chữ hay số. Gõ `65.5` thì nhận được chuỗi `"65.5"`, gõ `25` thì nhận được chuỗi `"25"`.
- `input()` không tự đoán kiểu dữ liệu. Muốn dùng như số thì lập trình viên phải tự ép kiểu bằng `int()` hoặc `float()`.

### Nguyên nhân

Ở dòng 3, giá trị trả về của `input()` được gán thẳng vào `weight` mà **không ép kiểu**, nên `weight` là chuỗi `"65.5"`.

Lỗi này khó phát hiện vì:
- `print()` hiển thị chuỗi `"65.5"` và số `65.5` giống hệt nhau (`65.5`).
- Chương trình không crash vì chưa có phép tính nào dùng `weight`. Lỗi chỉ bộc lộ khi tính toán, ví dụ:

```python
weight = "65.5"
height = 1.7
bmi = weight / (height ** 2)
# TypeError: unsupported operand type(s) for /: 'str' and 'float'
```

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân: ").strip()
# input() luôn trả về str -> ép kiểu sang float để lưu và tính toán
weight = float(input("Nhập cân nặng bệnh nhân (kg): "))

print("\n--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print(f"Bệnh nhân: {name_patient}")
print(f"Cân nặng đã nhập: {weight}")

# Kiểm tra kiểu dữ liệu của cân nặng trước khi lưu
print(f"Kiểu dữ liệu đang lưu là: {type(weight)}")
```

Các thay đổi:

1. **Sửa lỗi chính:** bọc `input()` trong `float()` để chuyển chuỗi sang số thực ngay khi nhập. Dùng `float` thay vì `int` vì cân nặng có phần thập phân (`65.5`). Nếu dùng `int("65.5")` sẽ bị `ValueError`.
2. Ghi rõ đơn vị `(kg)` trong lời nhắc nhập để tránh nhập nhầm đơn vị.
3. Dùng f-string cho phần in, thêm `.strip()` cho tên bệnh nhân, bỏ dấu cách thừa trước dấu `:`.

## Kết quả

Chạy `python script.py`:

```
--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---
Nhập tên bệnh nhân: Nguyễn Văn A
Nhập cân nặng bệnh nhân (kg): 65.5

--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---
Bệnh nhân: Nguyễn Văn A
Cân nặng đã nhập: 65.5
Kiểu dữ liệu đang lưu là: <class 'float'>
```

So sánh trước và sau khi sửa:

| | Legacy | Sau khi sửa |
|---|---|---|
| Giá trị hiển thị | `65.5` | `65.5` |
| Kiểu dữ liệu | `<class 'str'>` ❌ | `<class 'float'>` ✅ |
| Tính BMI được không | Không (`TypeError`) | Có |
