# Phần mềm Quản lý Bệnh nhân - Module Tiếp nhận Bệnh án

## Đề bài

Phòng khám Đa khoa đang tiếp nhận bệnh nhân thủ công bằng sổ giấy nên mất thời gian, dễ sai sót và khó tra cứu. Cần xây dựng module **Tiếp nhận Bệnh án** chạy trên giao diện dòng lệnh (CLI). Lễ tân nhập 3 thông tin bắt buộc của bệnh nhân mới:

- Họ và tên bệnh nhân
- Mã bệnh án (ví dụ: `BN1024`, `BA9901`)
- Khoa/Phòng khám chỉ định (ví dụ: Khoa Nội, Phòng Khám Mắt, Răng Hàm Mặt)

Sau đó hệ thống in **Phiếu khám bệnh điện tử** kèm thông báo xác nhận theo đúng chuẩn của phòng khám:

```
Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]
```

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

**Input:** nhập từ bàn phím bằng `input()`, cả 3 trường đều giữ kiểu **`str`**.

| Trường | Biến | Kiểu | Ví dụ | Lý do chọn kiểu |
|---|---|---|---|---|
| Họ và tên | `full_name` | `str` | `Nguyễn Văn An` | Dữ liệu văn bản |
| Mã bệnh án | `record_id` | `str` | `BN1024` | Gồm cả chữ và số, **không ép sang `int`** vì sẽ lỗi và mất phần chữ `BN` |
| Khoa/Phòng khám | `department` | `str` | `Khoa Nội` | Dữ liệu văn bản |

Bài này không cần ép kiểu vì không có trường nào dùng để tính toán.

**Output:** Phiếu khám bệnh điện tử in ra Console, gồm:
1. Khung tiêu đề phiếu.
2. Từng dòng thông tin, dấu `:` thẳng cột.
3. Dòng xác nhận đúng định dạng chuẩn: `Bệnh nhân: <Họ tên> - Mã BA: <Mã bệnh án> - Chuyển tới: <Khoa/Phòng>`.

### Đề xuất giải pháp

Chia xử lý thành 3 bước: **Nhập → Chuẩn hóa → Hiển thị**.

| Hàm / kỹ thuật | Công dụng trong bài |
|---|---|
| `input()` | Nhận dữ liệu lễ tân gõ từ bàn phím |
| `str.split()` + `" ".join(...)` | Bỏ khoảng trắng thừa ở đầu, cuối và giữa các từ (`"  nguyễn   văn an "` → `"nguyễn văn an"`) |
| `str.title()` | Viết hoa chữ cái đầu mỗi từ của họ tên (`"nguyễn văn an"` → `"Nguyễn Văn An"`) |
| `str.strip()` + `str.upper()` | Chuẩn hóa mã bệnh án thành chữ in hoa (`"bn1024"` → `"BN1024"`) để tra cứu thống nhất |
| f-string, `{:<15}`, `{:^50}` | Ghép chuỗi theo mẫu; căn trái nhãn và căn giữa tiêu đề cho phiếu gọn gàng |
| `"=" * 50` | Tạo đường kẻ khung cho phiếu |
| `print()` | Xuất phiếu ra màn hình |

### Thiết kế thuật toán (Pseudocode)

```
BẮT ĐẦU
    HIỂN THỊ tiêu đề "PHÒNG KHÁM ĐA KHOA - TIẾP NHẬN BỆNH NHÂN"

    // Bước 1: Nhập dữ liệu
    NHẬP full_name
    NHẬP record_id
    NHẬP department

    // Bước 2: Chuẩn hóa dữ liệu
    full_name  ← bỏ khoảng trắng thừa(full_name), viết hoa chữ cái đầu mỗi từ
    record_id  ← bỏ khoảng trắng đầu/cuối(record_id), chuyển IN HOA
    department ← bỏ khoảng trắng thừa(department)

    // Bước 3: Hiển thị phiếu khám
    HIỂN THỊ khung tiêu đề "PHIẾU KHÁM BỆNH ĐIỆN TỬ"
    HIỂN THỊ "Họ và tên  : " + full_name
    HIỂN THỊ "Mã bệnh án : " + record_id
    HIỂN THỊ "Khoa/Phòng : " + department
    HIỂN THỊ "Bệnh nhân: " + full_name + " - Mã BA: " + record_id + " - Chuyển tới: " + department
KẾT THÚC
```

## (2) Triển khai code

File: [`tiep_nhan_benh_an.py`](tiep_nhan_benh_an.py)

```python
# ===== BƯỚC 1: Nhập dữ liệu (input() luôn trả về str) =====
print("=" * 50)
print("   PHÒNG KHÁM ĐA KHOA - TIẾP NHẬN BỆNH NHÂN")
print("=" * 50)
full_name = input("Nhập họ và tên bệnh nhân     : ")
record_id = input("Nhập mã bệnh án (VD: BN1024) : ")
department = input("Nhập khoa/phòng khám chỉ định: ")

# ===== BƯỚC 2: Chuẩn hóa dữ liệu =====
full_name = " ".join(full_name.split()).title()   # bỏ khoảng trắng thừa, viết hoa chữ cái đầu
record_id = record_id.strip().upper()             # mã bệnh án viết hoa: bn1024 -> BN1024
department = " ".join(department.split())         # bỏ khoảng trắng thừa

# ===== BƯỚC 3: Hiển thị Phiếu khám bệnh điện tử =====
print()
print("=" * 50)
print(f"{'PHIẾU KHÁM BỆNH ĐIỆN TỬ':^50}")
print("=" * 50)
print(f"{'Họ và tên':<15}: {full_name}")
print(f"{'Mã bệnh án':<15}: {record_id}")
print(f"{'Khoa/Phòng':<15}: {department}")
print("-" * 50)

# Thông báo xác nhận theo đúng chuẩn định dạng của phòng khám
print(f"Bệnh nhân: {full_name} - Mã BA: {record_id} - Chuyển tới: {department}")
print("=" * 50)
```

Chạy chương trình:

```bash
python tiep_nhan_benh_an.py
```

## Kết quả

Lễ tân cố tình nhập thiếu chuẩn (chữ thường, thừa khoảng trắng), hệ thống vẫn chuẩn hóa và in phiếu đúng định dạng:

```
==================================================
   PHÒNG KHÁM ĐA KHOA - TIẾP NHẬN BỆNH NHÂN
==================================================
Nhập họ và tên bệnh nhân     :   nguyễn   văn an
Nhập mã bệnh án (VD: BN1024) : bn1024
Nhập khoa/phòng khám chỉ định:  Khoa  Nội

==================================================
             PHIẾU KHÁM BỆNH ĐIỆN TỬ
==================================================
Họ và tên      : Nguyễn Văn An
Mã bệnh án     : BN1024
Khoa/Phòng     : Khoa Nội
--------------------------------------------------
Bệnh nhân: Nguyễn Văn An - Mã BA: BN1024 - Chuyển tới: Khoa Nội
==================================================
```
