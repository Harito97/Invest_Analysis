import pandas as pd
from datetime import datetime

def convert_volume(volume):
    volume = str(volume)  # Đảm bảo biến là chuỗi
    if 'K' in volume:
        return int(float(volume.replace('K', '')) * 10**3)
    elif 'M' in volume:
        return int(float(volume.replace('M', '')) * 10**6)
    elif 'B' in volume:
        return int(float(volume.replace('B', '')) * 10**9)
    else:
        return int(float(volume))  # Nếu không có K hoặc M, chuyển đổi trực tiếp

def process_stock_index_vn(file_path, output_path):
    # Đọc dữ liệu và đổi tên cột
    df = pd.read_csv(file_path)
    df.columns = ["Date", "Close", "Open", "High", "Low", "Volume", "Change%"]

    # Chuyển đổi định dạng cột Date
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

    # Chuẩn hóa cột Volume
    # Thay thế giá trị NaN bằng 0 hoặc một giá trị khác phù hợp với ứng dụng của bạn
    df["Volume"] = df["Volume"].fillna("-1")
    df["Volume"] = df["Volume"].apply(convert_volume)

    # Chuẩn hóa cột Open, High, Low, Close, Change%
    # Xử lý cột "Open"
    df["Open"] = df["Open"].replace(",", "", regex=True)  # Loại bỏ dấu phẩy
    df["Open"] = df["Open"].astype(str).str.strip()  # Loại bỏ khoảng trắng
    df["Open"] = df["Open"].astype(float)  # Chuyển đổi sang float

    # Xử lý cột "High"
    df["High"] = df["High"].replace(",", "", regex=True)  # Loại bỏ dấu phẩy
    df["High"] = df["High"].astype(str).str.strip()  # Loại bỏ khoảng trắng
    df["High"] = df["High"].astype(float)  # Chuyển đổi sang float

    # Xử lý cột "Low"
    df["Low"] = df["Low"].replace(",", "", regex=True)  # Loại bỏ dấu phẩy
    df["Low"] = df["Low"].astype(str).str.strip()  # Loại bỏ khoảng trắng
    df["Low"] = df["Low"].astype(float)  # Chuyển đổi sang float

    # Xử lý cột "Close"
    df["Close"] = df["Close"].replace(",", "", regex=True)  # Loại bỏ dấu phẩy
    df["Close"] = df["Close"].astype(str).str.strip()  # Loại bỏ khoảng trắng
    df["Close"] = df["Close"].astype(float)  # Chuyển đổi sang float

    # Xử lý cột "Change%"
    df["Change%"] = df["Change%"].replace("%", "", regex=True)  # Loại bỏ ký hiệu %
    df["Change%"] = df["Change%"].astype(str).str.strip()  # Loại bỏ khoảng trắng
    df["Change%"] = df["Change%"].astype(float)  # Chuyển đổi sang float

    # Lưu dữ liệu đã chuẩn hóa
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    file_path = [
        "./raw/Dữ liệu Lịch sử HNX 30.csv",
        "./raw/Dữ liệu Lịch sử VN 30.csv",
        "./raw/Dữ liệu Lịch sử VN100.csv",
        "./raw/Dữ liệu Lịch sử VN Index.csv",
    ]
    output_path = [
        "./clean_HNX30.csv",
        "./clean_VN30.csv",
        "./clean_VN100.csv",
        "./clean_VNINDEX.csv",
    ]

    for i in range(len(file_path)):
        print(f"Processing {file_path[i]}...")
        process_stock_index_vn(file_path[i], output_path[i])
