import pandas as pd

def load_data(path):
    """
    Loads power consumption data from CSV file
    """
    data = pd.read_csv(path)
    return data

if __name__ == "__main__":
    df = load_data("../data/power_data.csv")
    print(df.head())
