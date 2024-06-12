import psycopg2

# Connection parameters
host = 'host_URL'
dbname = 'XXXXX'
user = 'XXXX'
password = 'XXXX'
sslmode = 'require'

# Establish connection
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    sslmode=sslmode
)

cur = conn.cursor()
for index, row in df.iterrows():
    query = sql.SQL('''
    INSERT INTO Table_name ("Datekey", "Client", "Provider","Patient name","Acct#/Pat#","Policy","0-30","31-60","61-90","91-120","121-150","150+","Pat/Ins Balance","0-30.1","31-60.1","61-90.1","91-120.1","121-150.1","150+.1","Pat/Ins Balance.1") VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    )
    
    cur.execute(query, (row['Datekey'], row['Client'], row['Provider'],row['Patient name'],row['Acct#/Pat#'],row['Policy'],row['0-30'],row['31-60'],row['61-90'],row['91-120'],row['121-150'],row['150+'],row['Pat/Ins Balance'],row['0-30.1'],row['31-60.1'],row['61-90.1'],row['91-120.1'],row['121-150.1'],row['150+.1'],row['Pat/Ins Balance.1']))
    conn.commit()
    print(f'{index} row added into DB')


conn.close()
