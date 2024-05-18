import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/11EXPJkrGHz42tF2ETm-OP9yIfAZ-8l3irl6IzBE1lnk/edit#gid=1903509374"
sheet_url_trf = sheet_url.replace('edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv("Supermarket Sales - Python Course (2) - supermarket_sales - Sheet1.csv")
df.head()
df.info()
print(df.columns)

# change type date
df_cleaned = df.copy()
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])
df_cleaned['Revenue'] = df_cleaned['Unit price'] * df_cleaned['Quantity']
print(df_cleaned.info())
df.head()

# check typo
df_cleaned['Gender'].value_counts()
for col_name in ['Payments', 'Branch', 'City', 'Customer type', 'Gender', 'Product line']:
    print(df_cleaned[col_name].value_counts(), '\n')

# replace
dict_typo =