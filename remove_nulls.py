import pandas as pd

df = pd.read_csv("messy_data.csv")

print("ROWS BEFORE:", len(df))

df_clean = df.dropna()

print("ROWS AFTER:", len(df_clean))
print()
print(df_clean)

df_clean.to_csv("no_nulls.csv", index=False)
print("\nSaved as no_nulls.csv")