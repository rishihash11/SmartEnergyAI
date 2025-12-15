from src.data_loader import load_data

data = load_data("data/power_data.csv")
print("Dataset loaded successfully")
print(data.head())
