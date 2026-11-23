import pandas as pd


def clean_data(input_file, output_file):
    # 1. UPLOAD
    df = pd.read_csv(input_file)
    report = {"rows_before": len(df)}

    # 2. REMOVE NULL VALUES
    report["nulls_found"] = int(df.isnull().sum().sum())
    df = df.dropna()

    # 3. REMOVE DUPLICATES
    before = len(df)
    df = df.drop_duplicates()
    report["duplicates_removed"] = before - len(df)

    # 4. EXPORT
    df.to_csv(output_file, index=False)
    report["rows_after"] = len(df)

    return report


result = clean_data("messy_data.csv", "final_clean.csv")

print("CLEANING REPORT")
for key, value in result.items():
    print(key, ":", value)