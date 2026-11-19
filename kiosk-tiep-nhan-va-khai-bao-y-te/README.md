# Kiosk Tiếp nhận và Khai báo Y tế

## Đề bài

Bệnh viện Đa khoa "Sức Khỏe Vàng" bị ùn tắc vì bệnh nhân phải xếp hàng hai lần: một lần ở quầy Lễ tân để khai thông tin cá nhân, một lần ở quầy Điều dưỡng để khai chỉ số sinh hiệu. Bệnh viện đặt một **Kiosk Khai Báo Tự Phục Vụ** ở sảnh để bệnh nhân tự nhập toàn bộ thông tin trong một lần. Kiosk cần:

- Giao tiếp thân thiện, rõ ràng để người không rành công nghệ cũng nhập đúng và hệ thống không bị crash.
- Tự động chuẩn hóa và ép kiểu dữ liệu, sau đó in **Phiếu Khám Bệnh Điện Tử** và **Log hệ thống** cho bộ phận IT kiểm tra kiểu dữ liệu.

Ràng buộc: tên biến tiếng Anh theo `snake_case`, code chia khối có comment (Khởi tạo, Thu thập dữ liệu, Xử lý ép kiểu, Hiển thị), prompt `input()` chi tiết kèm ví dụ.

## (1) Thiết kế kiến trúc và luồng dữ liệu

### Bảng thiết kế dữ liệu

Kiosk thu thập **8 trường** (4 thông tin cá nhân + 4 chỉ số sinh hiệu) và tính thêm 2 chỉ số.

| # | Tên biến (snake_case) | Nội dung input | Kiểu ban đầu | Kiểu mong muốn | Lý do |
|---|---|---|---|---|---|
| 1 | `patient_name` | Họ và tên bệnh nhân | `str` | `str` | Văn bản |
| 2 | `patient_id` | Mã bệnh nhân (VD: `BN1024`) | `str` | `str` | Gồm cả chữ và số |
| 3 | `birth_year` | Năm sinh (VD: `1990`) | `str` | `int` | Dùng để tính tuổi |
| 4 | `phone_number` | Số điện thoại (VD: `0912345678`) | `str` | `str` | Ép sang `int` sẽ mất số `0` đầu; không dùng để tính toán |
| 5 | `body_temperature` | Nhiệt độ cơ thể, °C (VD: `36.8`) | `str` | `float` | Có phần thập phân |
| 6 | `heart_rate` | Nhịp tim, nhịp/phút (VD: `78`) | `str` | `int` | Số nhịp đếm được, luôn nguyên |
| 7 | `body_weight` | Cân nặng, kg (VD: `62.5`) | `str` | `float` | Có phần thập phân |
| 8 | `body_height` | Chiều cao, cm (VD: `168`) | `str` | `float` | Dùng tính BMI, cho phép số lẻ |
| + | `patient_age` | *Tính:* năm hiện tại − `birth_year` | | `int` | |
| + | `body_mass_index` | *Tính:* cân nặng / (chiều cao m)² | | `float` | Minh họa dữ liệu đã ép kiểu dùng được để tính toán |

Giá trị nhập thô được lưu vào các biến tiền tố `raw_` (VD: `raw_heart_rate`), sau đó mới ép kiểu sang biến chính thức. Cách này giữ lại dữ liệu gốc để dễ dò lỗi.

### Luồng chương trình (Pseudocode)

```
BẮT ĐẦU
    // KHỐI 1: KHỞI TẠO
    Lấy thời gian hiện tại, năm hiện tại
    Hiển thị màn hình chào: tên bệnh viện + hướng dẫn "gõ câu trả lời rồi nhấn ENTER"

    // KHỐI 2: THU THẬP DỮ LIỆU
    Hiển thị "[PHẦN 1/2] THÔNG TIN CÁ NHÂN"
    NHẬP raw_patient_name, raw_patient_id, raw_birth_year, raw_phone_number
    Hiển thị "[PHẦN 2/2] CHỈ SỐ SINH HIỆU"
    NHẬP raw_body_temperature, raw_heart_rate, raw_body_weight, raw_body_height

    // KHỐI 3: XỬ LÝ ÉP KIỂU VÀ CHUẨN HÓA
    patient_name     ← bỏ khoảng trắng thừa, viết hoa chữ cái đầu
    patient_id       ← bỏ khoảng trắng, chuyển IN HOA
    phone_number     ← bỏ mọi dấu cách (giữ kiểu str)
    birth_year       ← int(raw_birth_year)
    heart_rate       ← int(raw_heart_rate)
    body_temperature ← float(đổi "," thành "." trong raw_body_temperature)
    body_weight      ← float(đổi "," thành "." trong raw_body_weight)
    body_height      ← float(đổi "," thành "." trong raw_body_height)
    patient_age      ← năm hiện tại − birth_year
    body_mass_index  ← làm tròn 1 chữ số(body_weight / (body_height / 100)²)

    // KHỐI 4: HIỂN THỊ
    IN Phiếu Khám Bệnh Điện Tử (thời gian, thông tin cá nhân, chỉ số sinh hiệu, BMI)
    IN Log hệ thống: với mỗi biến → tên biến | type(biến) | giá trị
KẾT THÚC
```

### Thiết kế câu hỏi `input()` (UX chống nhập sai)

Nguyên tắc thiết kế prompt:
- **Đánh số câu hỏi** (1 → 8) và **chia 2 phần** để người dùng biết mình đang ở đâu.
- **Ghi rõ đơn vị** (°C, nhịp/phút, kg, cm) và **dặn không gõ kèm đơn vị** để tránh nhập `62kg`.
- **Nói rõ định dạng**: "chỉ nhập 4 chữ số", "số nguyên, không có phần lẻ", "phần lẻ dùng dấu chấm".
- **Luôn có ví dụ cụ thể** `(VD: ...)` ở dòng thứ hai, ngay trước chỗ nhập.

| Trường | Prompt hiển thị trên Kiosk |
|---|---|
| Họ tên | `1. Họ và tên đầy đủ của Quý khách (VD: Nguyễn Văn An):` |
| Mã BN | `2. Mã bệnh nhân in trên thẻ khám (gồm chữ BN + các chữ số) (VD: BN1024):` |
| Năm sinh | `3. Năm sinh - chỉ nhập 4 chữ số, không nhập ngày/tháng (VD: 1990):` |
| Điện thoại | `4. Số điện thoại liên hệ - 10 chữ số, bắt đầu bằng số 0 (VD: 0912345678):` |
| Nhiệt độ | `5. Nhiệt độ cơ thể (độ C) - chỉ nhập số, phần lẻ dùng dấu chấm (VD: 36.8):` |
| Nhịp tim | `6. Nhịp tim (nhịp/phút) - chỉ nhập số nguyên, không có phần lẻ (VD: 78):` |
| Cân nặng | `7. Cân nặng (kg) - chỉ nhập số, không ghi chữ 'kg' (VD: 62.5):` |
| Chiều cao | `8. Chiều cao (cm) - chỉ nhập số, không ghi chữ 'cm' (VD: 168):` |

Ngoài prompt, khối xử lý còn **tự sửa các lỗi nhập phổ biến** để giảm nguy cơ crash:
- Thừa khoảng trắng đầu/cuối → `.strip()`
- Gõ dấu phẩy thập phân kiểu Việt Nam (`36,8`) → `.replace(",", ".")` trước khi `float()`
- Số điện thoại có dấu cách (`0912 345 678`) → `.replace(" ", "")`
- Tên/mã viết thường (`nguyễn văn an`, `bn1024`) → `.title()` / `.upper()`

## (2) Triển khai code

File: [`kiosk_khai_bao_y_te.py`](kiosk_khai_bao_y_te.py), một file duy nhất, chia 4 khối có comment.

**Khối 1: Khởi tạo:** hằng hiển thị, lấy thời gian tiếp nhận, màn hình chào.

```python
hospital_name = 'BỆNH VIỆN ĐA KHOA "SỨC KHỎE VÀNG"'
line_width = 60
current_time = datetime.now()
current_year = current_time.year
check_in_time = current_time.strftime("%H:%M - %d/%m/%Y")
```

**Khối 2: Thu thập dữ liệu:** 8 câu hỏi `input()`, lưu vào biến `raw_...` (kiểu `str`).

```python
raw_body_temperature = input(
    "5. Nhiệt độ cơ thể (độ C) - chỉ nhập số, phần lẻ dùng dấu chấm\n"
    "   (VD: 36.8): "
)
```

**Khối 3: Xử lý ép kiểu và chuẩn hóa**

```python
patient_name = " ".join(raw_patient_name.split()).title()
patient_id = raw_patient_id.strip().upper()
phone_number = raw_phone_number.strip().replace(" ", "")   # giữ str để không mất số 0 đầu

birth_year = int(raw_birth_year.strip())
heart_rate = int(raw_heart_rate.strip())

body_temperature = float(raw_body_temperature.strip().replace(",", "."))
body_weight = float(raw_body_weight.strip().replace(",", "."))
body_height = float(raw_body_height.strip().replace(",", "."))

patient_age = current_year - birth_year
body_mass_index = round(body_weight / (body_height / 100) ** 2, 1)
```

**Khối 4: Hiển thị:** hai phần tách biệt: Phiếu khám (cho bệnh nhân) và Log hệ thống (cho IT, in `type()` từng biến).

```python
print(f"{'heart_rate':<20} | {str(type(heart_rate)):<16} | {heart_rate}")
```

Chạy chương trình:

```bash
python kiosk_khai_bao_y_te.py
```

## Kết quả

Bệnh nhân nhập (cố tình có chữ thường, thừa khoảng trắng, dấu phẩy thập phân, số điện thoại có dấu cách):

```
[PHẦN 1/2] THÔNG TIN CÁ NHÂN
1. Họ và tên đầy đủ của Quý khách
   (VD: Nguyễn Văn An):   nguyễn   văn an
2. Mã bệnh nhân in trên thẻ khám (gồm chữ BN + các chữ số)
   (VD: BN1024): bn1024
3. Năm sinh - chỉ nhập 4 chữ số, không nhập ngày/tháng
   (VD: 1990): 1990
4. Số điện thoại liên hệ - 10 chữ số, bắt đầu bằng số 0
   (VD: 0912345678): 0912 345 678

[PHẦN 2/2] CHỈ SỐ SINH HIỆU (xem trên máy đo đặt cạnh Kiosk)
5. Nhiệt độ cơ thể (độ C) - chỉ nhập số, phần lẻ dùng dấu chấm
   (VD: 36.8): 36,8
6. Nhịp tim (nhịp/phút) - chỉ nhập số nguyên, không có phần lẻ
   (VD: 78): 78
7. Cân nặng (kg) - chỉ nhập số, không ghi chữ 'kg'
   (VD: 62.5): 62.5
8. Chiều cao (cm) - chỉ nhập số, không ghi chữ 'cm'
   (VD: 168): 168
```

Phiếu khám bệnh điện tử:

```
============================================================
                  PHIẾU KHÁM BỆNH ĐIỆN TỬ
             BỆNH VIỆN ĐA KHOA "SỨC KHỎE VÀNG"
============================================================
Thời gian tiếp nhận : 16:54 - 19/11/2026
------------------------------------------------------------
THÔNG TIN CÁ NHÂN
  Họ và tên         : Nguyễn Văn An
  Mã bệnh nhân      : BN1024
  Năm sinh (tuổi)   : 1990 (36 tuổi)
  Số điện thoại     : 0912345678
------------------------------------------------------------
CHỈ SỐ SINH HIỆU
  Nhiệt độ cơ thể   : 36.8 °C
  Nhịp tim          : 78 nhịp/phút
  Cân nặng          : 62.5 kg
  Chiều cao         : 168.0 cm
  Chỉ số BMI        : 22.1
============================================================
Cảm ơn Quý khách! Vui lòng mang phiếu này đến phòng khám.
============================================================
```

Log hệ thống (dành cho IT):

```
############################################################
             [SYSTEM LOG] KIỂM TRA KIỂU DỮ LIỆU
############################################################
Tên biến             | Kiểu dữ liệu     | Giá trị
------------------------------------------------------------
patient_name         | <class 'str'>    | Nguyễn Văn An
patient_id           | <class 'str'>    | BN1024
birth_year           | <class 'int'>    | 1990
phone_number         | <class 'str'>    | 0912345678
body_temperature     | <class 'float'>  | 36.8
heart_rate           | <class 'int'>    | 78
body_weight          | <class 'float'>  | 62.5
body_height          | <class 'float'>  | 168.0
patient_age          | <class 'int'>    | 36
body_mass_index      | <class 'float'>  | 22.1
############################################################
```

Tất cả các trường đều có đúng kiểu dữ liệu như bảng thiết kế.
