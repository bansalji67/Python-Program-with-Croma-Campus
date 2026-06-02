import pandas as pd
file=pd.read_excel(r"D:\Croma Campus\Python\Python-Program-with-Croma-Campus\Day-25\Financial_Sample.xlsx")
print(file)
print(file.columns)
print(file.isnull().sum())