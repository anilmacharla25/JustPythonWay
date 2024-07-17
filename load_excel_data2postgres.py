import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse


# Step 1: Define file path and database connection details
file_path = r"Z:\Business Intelligence\1-Automation\Discovery BH\TRL Short Database replaced with Serv Date Q1 2023- Q3 2023.xlsx"
sheet_name='TRL Short Consolidated'
database_type = 'postgresql'  # Change to your database type: 'mysql', 'postgresql', 'sqlite', etc.
user = 'Anil'
password = ''
host = ''  # Example: 'localhost'
database_name = 'Raw_Data_BI'
schema_name='Discovery_BH'
table_name = "discovery_bh_raw"
encoded_password = urllib.parse.quote(password)
chunk_size = 10000

# Create the database engine
engine = create_engine(f'{database_type}://{user}:{encoded_password}@{host}/{database_name}', connect_args={'options': f'-c search_path={schema_name}'})
print(engine)

#to check connection
try:
    with engine.connect() as connection:
        query = text('SELECT count(*) FROM "Discovery_BH"."discovery_bh_raw"')
        result = connection.execute(query)
        print(result)
        for row in result:
            print(f"Connection successful: {row}")
except Exception as e:
    print(f"Connection failed: {e}")

#to update data
# Define chunk size
# chunk_size = 25
# skip_rows = 0

# # Iterate over chunks
# while True:
#     # Read chunk of data
#     chunk = pd.read_excel(file_path, skiprows=skip_rows, nrows=chunk_size, header=1, sheet_name=sheet_name)
#     print(chunk.head())
#     chunk.to_sql(name=table_name, con=engine, if_exists='replace', index=False, schema=schema_name)
#     # Check if chunk is empty (end of file)
#     if chunk.empty:
#         break
# Define chunk size and initial skip rows
chunk_size = 25000  # Adjust chunk size based on your memory and performance requirements
skip_rows = 0
counter=0
while True:
    # Read chunk of data from Excel
    columns=['Posting Year', 'Posting Month', 'Service Year', 'Service Month',
       'PostDate', 'ServDate', 'Code', 'Description', 'Ledger Value', 'Place',
       'Name', 'Charges', 'Adjustments', 'Total Amount', 'Tran #', 'Type',
       'ServDate2', 'ChrgTr#', 'Service Year.1', 'Service Month.1',
       'Serv YYYY MM', 'Service Year Grp', 'Tag 1', 'Tag 2', 'Tag 3',
       'Location Name', 'Division', 'Brand', 'OPRTC']
    if counter==0:
        chunk = pd.read_excel(file_path, skiprows=skip_rows, nrows=chunk_size, header=1, sheet_name=sheet_name)
    else:
        chunk = pd.read_excel(file_path, skiprows=skip_rows, nrows=chunk_size, header=None, sheet_name=sheet_name)
        chunk.columns=columns
    if chunk.empty:
        break
    print(chunk.head())
    # Write chunk to SQL table
    chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False, schema=schema_name)

    # Update skip_rows for the next chunk
    skip_rows += chunk_size

    # Print progress or perform additional processing
    print(f"Processed {skip_rows} rows")
    counter+=1
# Optionally, print a completion message
print("Data migration complete.")
