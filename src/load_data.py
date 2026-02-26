import pandas as pd
from pathlib import Path

# Define path to dataset
DATA_DIR = Path("data/raw/ServerMachineDataset/train")
FILE_NAME = "machine-1-1.txt"

file_path = DATA_DIR / FILE_NAME

# Load the space-separated file (no headers in raw data)
df = pd.read_csv(file_path, sep=",", header=None)

# Assign generic column names
df.columns = [f"sensor_{i+1}" for i in range(df.shape[1])]

print("Data loaded successfully")
print("Shape (rows, columns):", df.shape)
print("\nFirst 5 rows:")
print(df.head())