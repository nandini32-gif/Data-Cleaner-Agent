import pandas as pd

df = pd.read_csv("messy_data.csv")

print("FIRST ROWS")
print(df.head())

print("\nSHAPE (rows, columns)")
print(df.shape)

print("\nMISSING VALUES PER COLUMN")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())