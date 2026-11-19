print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---")
name_patient = input("Nhập tên bệnh nhân: ").strip()
age = int(input("Mời bạn nhập tuổi: "))
symptom = input("Mời bạn nhập triệu chứng bệnh: ").strip()

print("\n--- PHIẾU KHÁM BỆNH ---")
print(f"Tên bệnh nhân: {name_patient}")
print(f"Tuổi: {age}")
print(f"Triệu chứng: {symptom}")
