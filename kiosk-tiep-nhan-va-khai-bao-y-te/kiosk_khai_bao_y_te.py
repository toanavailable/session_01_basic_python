"""Kiosk Tiếp nhận và Khai báo Y tế - Bệnh viện Đa khoa "Sức Khỏe Vàng"."""

from datetime import datetime

# =====================================================================
# KHỐI 1: KHỞI TẠO
# =====================================================================
hospital_name = 'BỆNH VIỆN ĐA KHOA "SỨC KHỎE VÀNG"'
line_width = 60
current_time = datetime.now()
current_year = current_time.year
check_in_time = current_time.strftime("%H:%M - %d/%m/%Y")

print("=" * line_width)
print(f"{hospital_name:^{line_width}}")
print(f"{'KIOSK KHAI BÁO Y TẾ TỰ PHỤC VỤ':^{line_width}}")
print("=" * line_width)
print("Xin chào Quý khách! Vui lòng trả lời lần lượt các câu hỏi bên dưới.")
print("Gõ câu trả lời rồi nhấn phím ENTER để sang câu tiếp theo.")
print("-" * line_width)

# =====================================================================
# KHỐI 2: THU THẬP DỮ LIỆU (input() luôn trả về chuỗi str)
# =====================================================================
print("\n[PHẦN 1/2] THÔNG TIN CÁ NHÂN")
raw_patient_name = input(
    "1. Họ và tên đầy đủ của Quý khách\n"
    "   (VD: Nguyễn Văn An): "
)
raw_patient_id = input(
    "2. Mã bệnh nhân in trên thẻ khám (gồm chữ BN + các chữ số)\n"
    "   (VD: BN1024): "
)
raw_birth_year = input(
    "3. Năm sinh - chỉ nhập 4 chữ số, không nhập ngày/tháng\n"
    "   (VD: 1990): "
)
raw_phone_number = input(
    "4. Số điện thoại liên hệ - 10 chữ số, bắt đầu bằng số 0\n"
    "   (VD: 0912345678): "
)

print("\n[PHẦN 2/2] CHỈ SỐ SINH HIỆU (xem trên máy đo đặt cạnh Kiosk)")
raw_body_temperature = input(
    "5. Nhiệt độ cơ thể (độ C) - chỉ nhập số, phần lẻ dùng dấu chấm\n"
    "   (VD: 36.8): "
)
raw_heart_rate = input(
    "6. Nhịp tim (nhịp/phút) - chỉ nhập số nguyên, không có phần lẻ\n"
    "   (VD: 78): "
)
raw_body_weight = input(
    "7. Cân nặng (kg) - chỉ nhập số, không ghi chữ 'kg'\n"
    "   (VD: 62.5): "
)
raw_body_height = input(
    "8. Chiều cao (cm) - chỉ nhập số, không ghi chữ 'cm'\n"
    "   (VD: 168): "
)

# =====================================================================
# KHỐI 3: XỬ LÝ ÉP KIỂU VÀ CHUẨN HÓA
# =====================================================================
# Chuỗi văn bản: bỏ khoảng trắng thừa, chuẩn hóa chữ hoa/thường
patient_name = " ".join(raw_patient_name.split()).title()
patient_id = raw_patient_id.strip().upper()
phone_number = raw_phone_number.strip().replace(" ", "")   # giữ str để không mất số 0 đầu

# Số nguyên (int)
birth_year = int(raw_birth_year.strip())
heart_rate = int(raw_heart_rate.strip())

# Số thực (float): đổi dấu phẩy thành dấu chấm phòng khi người dùng gõ "36,8"
body_temperature = float(raw_body_temperature.strip().replace(",", "."))
body_weight = float(raw_body_weight.strip().replace(",", "."))
body_height = float(raw_body_height.strip().replace(",", "."))

# Chỉ số tính thêm từ dữ liệu đã ép kiểu
patient_age = current_year - birth_year                       # int
body_mass_index = round(body_weight / (body_height / 100) ** 2, 1)  # float

# =====================================================================
# KHỐI 4: HIỂN THỊ
# =====================================================================
# --- Phần A: Phiếu khám bệnh điện tử (dành cho bệnh nhân) ---
label_width = 20
print("\n" + "=" * line_width)
print(f"{'PHIẾU KHÁM BỆNH ĐIỆN TỬ':^{line_width}}")
print(f"{hospital_name:^{line_width}}")
print("=" * line_width)
print(f"{'Thời gian tiếp nhận':<{label_width}}: {check_in_time}")
print("-" * line_width)
print("THÔNG TIN CÁ NHÂN")
print(f"  {'Họ và tên':<{label_width - 2}}: {patient_name}")
print(f"  {'Mã bệnh nhân':<{label_width - 2}}: {patient_id}")
print(f"  {'Năm sinh (tuổi)':<{label_width - 2}}: {birth_year} ({patient_age} tuổi)")
print(f"  {'Số điện thoại':<{label_width - 2}}: {phone_number}")
print("-" * line_width)
print("CHỈ SỐ SINH HIỆU")
print(f"  {'Nhiệt độ cơ thể':<{label_width - 2}}: {body_temperature} °C")
print(f"  {'Nhịp tim':<{label_width - 2}}: {heart_rate} nhịp/phút")
print(f"  {'Cân nặng':<{label_width - 2}}: {body_weight} kg")
print(f"  {'Chiều cao':<{label_width - 2}}: {body_height} cm")
print(f"  {'Chỉ số BMI':<{label_width - 2}}: {body_mass_index}")
print("=" * line_width)
print("Cảm ơn Quý khách! Vui lòng mang phiếu này đến phòng khám.")
print("=" * line_width)

# --- Phần B: Log hệ thống (dành cho IT) ---
print("\n" + "#" * line_width)
print(f"{'[SYSTEM LOG] KIỂM TRA KIỂU DỮ LIỆU':^{line_width}}")
print("#" * line_width)
print(f"{'Tên biến':<20} | {'Kiểu dữ liệu':<16} | Giá trị")
print("-" * line_width)
print(f"{'patient_name':<20} | {str(type(patient_name)):<16} | {patient_name}")
print(f"{'patient_id':<20} | {str(type(patient_id)):<16} | {patient_id}")
print(f"{'birth_year':<20} | {str(type(birth_year)):<16} | {birth_year}")
print(f"{'phone_number':<20} | {str(type(phone_number)):<16} | {phone_number}")
print(f"{'body_temperature':<20} | {str(type(body_temperature)):<16} | {body_temperature}")
print(f"{'heart_rate':<20} | {str(type(heart_rate)):<16} | {heart_rate}")
print(f"{'body_weight':<20} | {str(type(body_weight)):<16} | {body_weight}")
print(f"{'body_height':<20} | {str(type(body_height)):<16} | {body_height}")
print(f"{'patient_age':<20} | {str(type(patient_age)):<16} | {patient_age}")
print(f"{'body_mass_index':<20} | {str(type(body_mass_index)):<16} | {body_mass_index}")
print("#" * line_width)
