import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw/ServerMachineDataset/train")
PROCESSED_DIR = Path("data/processed/train")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

for file in DATA_DIR.glob("*.txt"):
    df = pd.read_csv(file, sep=",", header=None)
    df.columns = [f"sensor_{i+1}" for i in range(df.shape[1])]
    
    processed_file = PROCESSED_DIR / f"{file.stem}.csv"
    df.to_csv(processed_file, index=False)
    print(f"{file.name} processed and saved to {processed_file}")

