#pandas remove duplicates test
import time as t
import pyautogui
from datetime import date,datetime
from datetime import *
import subprocess
import datetime
import ctypes
import pendulum as p
import os,sys
import pyodbc
import pytz
import pandas as pd
name='gverma'
date='09/14/2022'
#database connection
cnxn=pyodbc.connect("DSN=test3;UID=sa;PWD=")
cursor = cnxn.cursor()
qry="SELECT * FROM raw_tracker_data where (user_name='%s' and date='%s')" %(name,date)
#val=(name,today,login_time,last_active_at,last_break_time,total_locked_time,total_time_spent)
#cursor.execute(qry)
df = pd.read_sql_query(qry,con=cnxn)
print(df.size)
print(df)
df1=df.drop_duplicates( "break_start_at" , keep='first')
print(df1.size)
print(df1)
if df.size==df1.size:
    print(f'there is no duplicate record with name {name}')
else:
    df1.to_sql('raw_data_new', engine=cnxn, chunksize=1000)
    print('need to do time operations and update the value in track hour table')
    
    #df1['total_break_time'] = pd.to_datetime(df1['total_break_time'], format=r'%H:%M:%S').dt.time
    print(df1)
    #total=pd.to_timedelta(df1["total_break_time"]).sum()
    #print(df1['total_break_time'].sum())
    

    break_column = df1['total_break_time']
    print(break_column)

    total_break_taken=0
    for interval in break_column:
        #print(type(interval))
        #print(interval)
        h,m,s = interval.split(':')
        each_break=int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
        total_break_taken+=each_break
    print(total_break_taken)
    final_break_time=t.strftime('%H:%M:%S', t.gmtime(total_break_taken))
    print(final_break_time)
    print(type(final_break_time))
    qry1="UPDATE track_hours SET total_locked_time='%s' where (user_name='%s' and date='%s')" %(final_break_time,name,date)
    cursor.execute(qry1)
                
    
        
        
   

##rows=cursor.fetchall()
###print(rows)
##for row in rows:
##    print(row)
cnxn.commit()
cnxn.close()

