print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân: ").strip()
# input() luôn trả về str -> ép kiểu sang float để lưu và tính toán
weight = float(input("Nhập cân nặng bệnh nhân (kg): "))

print("\n--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print(f"Bệnh nhân: {name_patient}")
print(f"Cân nặng đã nhập: {weight}")

# Kiểm tra kiểu dữ liệu của cân nặng trước khi lưu
print(f"Kiểu dữ liệu đang lưu là: {type(weight)}")
