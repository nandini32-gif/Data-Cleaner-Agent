import pandas as pd

df = pd.read_csv("no_nulls.csv")

print("ROWS BEFORE:", len(df))
print("DUPLICATES FOUND:", df.duplicated().sum())

df_clean = df.drop_duplicates()

print("ROWS AFTER:", len(df_clean))
print()
print(df_clean)

df_clean.to_csv("clean_data.csv", index=False)
print("\nSaved as clean_data.csv")