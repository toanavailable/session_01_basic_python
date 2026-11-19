# Quản lý phòng khám - Sửa lỗi in Phiếu khám bệnh

## Đề bài

Phần mềm tiếp nhận bệnh nhân của phòng khám cho lễ tân nhập **họ tên**, **tuổi** và **triệu chứng**, sau đó in ra **Phiếu khám bệnh**. Chương trình chạy không crash, không có lỗi cú pháp, nhưng thông tin trên phiếu bị in sai vị trí:

| Dữ liệu nhập | Phiếu in ra (sai) |
|---|---|
| Họ tên: Nguyễn Văn A | Họ tên bệnh nhân: Đau đầu |
| Tuổi: 25 | Tuổi: Nguyễn Văn A |
| Triệu chứng: Đau đầu | Triệu chứng: 25 |

Yêu cầu: (1) phân tích lỗi bằng cách dò luồng thực thi; (2) viết lại mã nguồn đúng.

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py)

```python
print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ');
name_patient = input('Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input('Mời bạn nhập triệu chứng bênh: ');

print(' -- PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', symptom);
print('Tuổi:', name_patient);
print ('Triệu chứng:', age);
```

## (1) Phân tích lỗi

### Dò luồng thực thi (trace code)

Với dữ liệu nhập `Nguyễn Văn A`, `25`, `Đau đầu`:

| Dòng | Câu lệnh | Trạng thái biến sau khi chạy |
|---|---|---|
| 2 | `name_patient = input(...)` | `name_patient = "Nguyễn Văn A"` (str) ✅ |
| 3 | `age = int(input(...))` | `age = 25` (int) ✅ |
| 4 | `symptom = input(...)` | `symptom = "Đau đầu"` (str) ✅ |
| 7 | `print('Tên bệnh nhân:', symptom)` | In ra `Tên bệnh nhân: Đau đầu` ❌ |
| 8 | `print('Tuổi:', name_patient)` | In ra `Tuổi: Nguyễn Văn A` ❌ |
| 9 | `print('Triệu chứng:', age)` | In ra `Triệu chứng: 25` ❌ |

Kết luận: **phần nhập liệu (dòng 2–4) hoàn toàn đúng**, mỗi biến lưu đúng dữ liệu. Lỗi chỉ nằm ở **phần in phiếu (dòng 7–9)**.

### Nguyên nhân gây lỗi logic

Ở phần in phiếu, mỗi nhãn được ghép **nhầm biến**, các biến bị xoay vòng lệch một vị trí:

| Nhãn | Biến đang dùng (sai) | Biến đúng |
|---|---|---|
| `Tên bệnh nhân:` | `symptom` | `name_patient` |
| `Tuổi:` | `name_patient` | `age` |
| `Triệu chứng:` | `age` | `symptom` |

### Vì sao chương trình không crash?

- **Không có lỗi cú pháp:** dấu `;` cuối dòng và khoảng trắng trong `print (...)` đều hợp lệ trong Python, chỉ là không cần thiết.
- **Không có lỗi khi chạy (runtime):** cả 3 biến đều đã được gán giá trị trước khi dùng nên không có `NameError`. `print()` in được mọi kiểu dữ liệu (`str`, `int`…) nên dù truyền nhầm biến kiểu `int` vào chỗ của chuỗi cũng không sinh `TypeError`.
- Python chỉ kiểm tra câu lệnh có **hợp lệ** hay không, không biết **ý nghĩa** của biến. Tên biến `age` hay `symptom` chỉ có ý nghĩa với người lập trình. Vì vậy đây là **lỗi logic**: chương trình chạy trọn vẹn nhưng kết quả sai so với nghiệp vụ.

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---")
name_patient = input("Nhập tên bệnh nhân: ").strip()
age = int(input("Mời bạn nhập tuổi: "))
symptom = input("Mời bạn nhập triệu chứng bệnh: ").strip()

print("\n--- PHIẾU KHÁM BỆNH ---")
print(f"Tên bệnh nhân: {name_patient}")
print(f"Tuổi: {age}")
print(f"Triệu chứng: {symptom}")
```

Các thay đổi:

1. **Sửa lỗi chính:** ghép đúng nhãn với biến tương ứng (`name_patient` → Tên, `age` → Tuổi, `symptom` → Triệu chứng).
2. Dùng **f-string** để nhãn và biến nằm cạnh nhau trong cùng một chuỗi, dễ đọc và khó ghép nhầm hơn.
3. Bỏ dấu `;` thừa, bỏ khoảng trắng giữa `print` và `(` theo chuẩn PEP 8, thống nhất dùng nháy kép.
4. Thêm `.strip()` để loại bỏ khoảng trắng thừa khi nhập chuỗi.
5. Sửa lỗi chính tả trong lời nhắc: "bênh" → "bệnh"; thống nhất tiêu đề phiếu `--- PHIẾU KHÁM BỆNH ---`.

## Kết quả

Chạy `python script.py` với cùng bộ dữ liệu:

```
--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---
Nhập tên bệnh nhân: Nguyễn Văn A
Mời bạn nhập tuổi: 25
Mời bạn nhập triệu chứng bệnh: Đau đầu

--- PHIẾU KHÁM BỆNH ---
Tên bệnh nhân: Nguyễn Văn A
Tuổi: 25
Triệu chứng: Đau đầu
```

Thông tin trên phiếu đã khớp chính xác với dữ liệu nhập vào.
