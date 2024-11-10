import pandas as pd

# Đọc dữ liệu từ file
file_path = './clean_step0/clean_0.csv'
df = pd.read_csv(file_path)

# Kiểm tra và chuẩn hóa cột tên cột nếu cần (thay khoảng trắng và dấu xuống dòng)
df.columns = [col.strip() for col in df.columns]

# Xác định các năm đã có trong dữ liệu và bổ sung những năm còn thiếu (1990-1994)
existing_years = set(map(str, range(1990, 1995)))
missing_years = existing_years.difference(df.columns)
for year in missing_years:
    df[year] = None  # Bổ sung cột cho năm thiếu

# Chuyển định dạng dữ liệu cột chỉ số thành số thực hoặc số nguyên
for col in df.columns[2:]:  # Bỏ qua cột "Chỉ_tiêu" và "Đơn_vị_tính"
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Xử lý dữ liệu trống: đổi dấu '-' thành -1 hoặc 0 tùy theo loại dữ liệu
# Giả sử các cột liên quan đến CPI có chữ "CPI" trong tên chỉ tiêu
cpi_related = df['Chỉ_tiêu'].str.contains('CPI', case=False, na=False)

for col in df.columns[2:]:
    # Đặt giá trị là 0 cho các cột liên quan đến CPI, và -1 cho các cột khác
    df.loc[~cpi_related, col] = df.loc[~cpi_related, col].fillna(-1)
    df.loc[cpi_related, col] = df.loc[cpi_related, col].fillna(0)

# Sắp xếp lại các cột để dễ truy cập dữ liệu theo thứ tự năm
sorted_columns = ['Chỉ_tiêu', 'Đơn_vị_tính'] + sorted(df.columns[2:], key=lambda x: int(x))
df = df[sorted_columns]

# Lưu lại file CSV đã được chuẩn hóa
output_path = './cleaned_data.csv'
df.to_csv(output_path, index=False)

print(f"Dữ liệu đã được chuẩn hóa và lưu tại {output_path}")
