"""Module Tiếp nhận Bệnh án: nhập thông tin bệnh nhân và in Phiếu khám bệnh điện tử."""

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
