import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")
print("Average score:", df['score'].mean())
