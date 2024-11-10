import yfinance as yf
import pandas as pd
import os

# Danh sách các mã chỉ số và tên file tương ứng
indices = {
    # "^GSPC": "SP500",
    # "VND=X": "VNDUSD",
    # "BTC-USD": "BTCUSD",
    # "ETH-USD": "ETHUSD",
    # "BZ=F": "BrentCrudeOil",
    # "CL=F": "CrudeOil",
    # "GC=F": "Gold",
    # "SI=F": "Silver",
    # "^TYX": "30YearTreasury",
    # "^TNX": "10YearTreasury",
    # "^FVX": "5YearTreasury",
    # "^IRX": "3MonthTreasury"
}

#^VNINDEX.VN     # VNINDEX.VN
#VND=X           # VND/USD
# ^GSPC           # S&P 500
# BTC-USD         # BTC-USD
# ETH-USD         # ETH-USD
# BZ=F            # Brent Crude Oil
# CL=F            # Crude Oil
# GC=F            # Gold
# SI=F            # Silver
# ^TYX            # 30-Year Treasury
# ^TNX            # 10-Year Treasury
# ^FVX            # 5-Year Treasury
# ^IRX            # 3-Month Treasury (13 weeks)

# Tạo thư mục để lưu dữ liệu
output_dir = "finance_data"
os.makedirs(output_dir, exist_ok=True)

for ticker, filename in indices.items():
    print(f"Downloading data for {ticker}...")
    # Tải dữ liệu lịch sử
    data = yf.download(ticker, period="max")

    # Lưu dữ liệu vào file CSV
    csv_path = os.path.join(output_dir, f"{filename}.csv")
    data.to_csv(csv_path)

    # Tính toán giá trị lớn nhất, nhỏ nhất cho mỗi cột và chuẩn bị ghi chú
    column_max = data.max()
    column_min = data.min()

    # Tạo file TXT với chú thích và thông tin giá trị lớn nhất, nhỏ nhất
    txt_path = os.path.join(output_dir, f"{filename}_info.txt")
    with open(txt_path, "w") as file:
        # Ghi chú thích các cột thuộc tính
        file.write("Column Descriptions:\n")
        file.write("Date: Trading date\n")
        file.write("Open: Opening price\n")
        file.write("High: Highest price\n")
        file.write("Low: Lowest price\n")
        file.write("Close: Closing price\n")
        file.write("Adj Close: Adjusted closing price\n")
        file.write("Volume: Trading volume\n\n")

        # Ghi giá trị lớn nhất và nhỏ nhất cho mỗi cột
        file.write("Max and Min Values for Each Column:\n")
        for col in data.columns:
            file.write(f"{col}:\n")
            file.write(f"  Max: {column_max[col]}\n")
            file.write(f"  Min: {column_min[col]}\n")
            file.write("\n")
