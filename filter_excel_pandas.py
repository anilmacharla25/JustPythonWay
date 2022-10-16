#filter excel data and use column values in dropdown in tkinter
import pandas as pd
file_location=r"C:\Users\prave\Downloads\payer_names.xlsx"
df=pd.read_excel(file_location)
print(df)
df1=df[df['payer name']=='TOX']
print(df1)
dd1=df1['test type'].tolist()
print(dd1)
df2=df1[df1['test type']=='<35']
print(df2)
