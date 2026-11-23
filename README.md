# Data-Cleaner-Agent
A simple web app that cleans and merges messy datasets. Upload a CSV or Excel file, choose how to handle missing values and duplicates, and download the cleaned data in one click.

# Features
Quick Clean
• Upload CSV or Excel files (.csv, .xlsx, .xls)
• Handle missing values: remove rows, fill them (numbers with the median, text with "Unknown"), or leave as is
• Remove duplicate rows
• Trim extra spaces in text columns
• See a summary: rows before, nulls found, duplicates removed, rows after, and time taken
• Export the cleaned data as CSV

Smart Merge
• Stack two files with the same columns, or join them on a shared column (inner, left or outer join)
• Download the merged file as CSV

# Recent Activity
• Log of the cleaning and merging actions done in the current session

# Tech Stack
• Python
• Streamlit
• Pandas
• OpenPyXL (Excel file support)

# How to Run
1. Download or clone this repository.
2. Install the requirements:
pip install -r requirements.txt
3. Start the app:
python -m streamlit run app.py
4. Open the link shown in the terminal (usually http://localhost:8501).

# Try It
Use the sample file messy_data.csv:
1. Open Quick Clean and upload the file.
2. Choose Remove rows and click Start Cleaning to see the summary.
3. Choose Fill instead to keep the rows with missing values.

# Author
Nandini Yogesh Tapase
Data Analytics , Fortune cloud technologies 
LinkedIn | GitHub
