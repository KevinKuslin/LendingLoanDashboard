import pandas as pd

df = pd.read_parquet("data/accepted_raw.parquet")
print(df.shape)