import pandas as pd
import numpy as np

data = {
    "name":   ["Asha", "Ravi", "Ravi", None, "Meena", "Karan"],
    "age":    [25, 30, 30, 22, np.nan, 28],
    "city":   ["Pune", "Mumbai", "Mumbai", "Delhi", "Pune", None],
    "salary": [50000, 60000, 60000, 45000, 52000, np.nan],
}

df = pd.DataFrame(data)
df.to_csv("messy_data.csv", index=False)
print("messy_data.csv created")