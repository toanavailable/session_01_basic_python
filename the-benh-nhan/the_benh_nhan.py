"""Chương trình nhập thông tin bệnh nhân và in thẻ bệnh nhân trên Console."""

import random

# Lưu các mã đã cấp trong lần chạy này để đảm bảo mã không bị trùng
used_ids = set()


def generate_patient_id(birth_year):
    """Tạo mã theo định dạng: BN + năm sinh + 3 số ngẫu nhiên (không trùng)."""
    while True:
        random_part = random.randint(100, 999)
        patient_id = f"BN{birth_year}{random_part}"
        if patient_id not in used_ids:
            used_ids.add(patient_id)
            return patient_id


def show_field(label, value, suffix=""):
    """In một dòng của thẻ: nhãn, giá trị và kiểu dữ liệu lấy bằng type()."""
    print(f"{label:<11}: {value}{suffix} ({type(value).__name__})")


# 1. Nhập thông tin bệnh nhân
name = input("Nhập tên bệnh nhân: ").strip()
gender = input("Nhập giới tính: ").strip()
birth_year = input("Nhập năm sinh: ").strip()
phone = input("Nhập số điện thoại: ").strip()
email = input("Nhập email: ").strip()
symptom = input("Nhập triệu chứng ban đầu: ").strip()
cost = input("Nhập chi phí khám: ").strip()

# 2. Ép kiểu dữ liệu: năm sinh -> int, chi phí -> float, các trường khác giữ str
birth_year = int(birth_year)
cost = float(cost)

# 3. Tạo mã bệnh nhân tự động
patient_id = generate_patient_id(birth_year)

# 4 + 5. Hiển thị thẻ bệnh nhân kèm kiểu dữ liệu của từng trường
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
