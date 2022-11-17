#scrapping a table of web page using bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.nfl.com/standings/league/2019/REG'
page=requests.get(url)
print(page)
soup=BeautifulSoup(page.text,'lxml')
table=soup.find('table',{'summary':'Standings - Detailed View'})
print(table.prettify())
headers=[]
for i in table.find_all('th'):
    title=i.text.strip()
    headers.append(title)
print(headers)
df=pd.DataFrame(columns=headers)
print(df)

for row in table.find_all('tr')[1:]:
    first_td=row.find_all('td')[0].text.strip()
    data=row.find_all('td')[1:]
    row_data=[td.text.strip() for td in data]
    row_data.insert(0,first_td)
    length=len(df)
    df.loc[length]=row_data

print(df)
df.to_excel(r"C:\Users\AMacharla\Documents\filter3.xlsx")

    

