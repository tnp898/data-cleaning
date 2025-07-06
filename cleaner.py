import pandas as pd

df = pd.read_csv("data/raw_data.csv")
df_cleaned = df.dropna()
df_cleaned.to_csv("data/cleaned_data.csv", index=False)
