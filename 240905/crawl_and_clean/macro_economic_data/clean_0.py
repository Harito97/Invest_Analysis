import csv

def clean_data_csv(file_path, output_path):
    with open(file_path, "r") as file:
        data = []
        for line in file:
            if line.startswith("#"):
                continue
            data.append(line.strip().split())
        print(data)

    with open(output_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print("Write to file successfully!")


# file_path = "./raw/TyGia.csv"
# output_path = "./clean_step0/clean_TyGia.csv"

# file_path = "./raw/DanSo_LaoDong.csv"
# output_path = "./clean_step0/clean_DanSo_LaoDong.csv"

# file_path = "./raw/CPI.csv"
# output_path = "./clean_step0/clean_CPI.csv"

file_path = "./raw/GDP.csv"
output_path = "./clean_step0/clean_GDP.csv"
clean_data_csv(file_path, output_path)
