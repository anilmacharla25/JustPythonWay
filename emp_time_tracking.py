#python  tracker  scrpit 1
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

user32 = ctypes.windll.User32
#function to check if system is locked or not and returns true if locked 
def isLocked():
    return user32.GetForegroundWindow() == 0

#function indirectly holds the program if condition becomes True
def hold_on():
    while True:
        if isLocked()==False:
            t.sleep(2)
            os.system("shutdown -l")
            t.sleep(10)
            sys.exit("user taken continuous 3 hrs break")
        
name=os.getlogin( )
print(name)
today = date.today()
today=today.strftime("%d-%m-%Y")
print("date:",today)
print(type(today))

now = datetime.datetime.now().replace(microsecond=0)
login_time=now.time()
login_time=login_time.strftime("%H:%M:%S")
print("login_time:",login_time)

#sample
last_active_at='00:00:00'
last_break_time="00:00:00"
total_locked_time='00:00:00'
total_time_spent="00:00:00"


cnxn=pyodbc.connect('DSN=test3;UID=DBADMINNAME;PWD=PWD')
cursor = cnxn.cursor()
##cursor.execute('''drop table track_hours''')
##cursor.execute('''
##CREATE TABLE track_hours (
##        ID int IDENTITY(1,1) NOT NULL PRIMARY KEY ,
##        user_name nvarchar(50),
##        date nvarchar(50) ,
##        login_time nvarchar(50),
##        last_active_at nvarchar(50),
##        most_recent_break nvarchar(50),
##        total_locked_time nvarchar(50),
##        total_time_spent nvarchar(50)
##        
##        )
##''')

sql="INSERT INTO track_hours (user_name, date, login_time,last_active_at,most_recent_break,total_locked_time,total_time_spent) VALUES (?,?,?,?,?,?,?)"
val=(name,today,login_time,last_active_at,last_break_time,total_locked_time,total_time_spent)

cursor.execute(sql,val)
cnxn.commit()
record_id = cursor.execute('SELECT @@IDENTITY AS id;').fetchone()[0]

cnxn.close()
print(record_id)

t.sleep(1)
locked_time=0
while True:
    cnxn=pyodbc.connect('DSN=test3;UID=sa;PWD=PWD')
    cursor = cnxn.cursor()
    
    now = datetime.datetime.now().replace(microsecond=0)
    current_time=now.time()
    current_time=current_time.strftime("%H:%M:%S")
    last_active_at=current_time
    s1=datetime.datetime.strptime(login_time,"%H:%M:%S")
    s2=datetime.datetime.strptime(current_time,"%H:%M:%S")
    total_sec=(s2-s1).seconds
    print(total_sec)
    total_time_spent=t.strftime('%H:%M:%S', t.gmtime(total_sec))
    print("total time spent",total_time_spent)
    if total_sec<50400:#more than 14 hrs of total time spent
        cursor.execute ("UPDATE track_hours SET last_active_at='%s',total_time_spent='%s' WHERE ID='%d'" %(last_active_at,total_time_spent,record_id))
        cnxn.commit()
        cnxn.close()
    else:
        os.system("shutdown -l")
        t.sleep(10)
        
        
        
        
    t.sleep(1)
    
    if isLocked()==True:
        now = datetime.datetime.now().replace(microsecond=0)
        locked_at=now.time()
        locked_at=locked_at.strftime("%H:%M:%S")
        print("locked_at",locked_at)
        
        while isLocked()==True:
            t.sleep(1)
            now = datetime.datetime.now().replace(microsecond=0)
            still_locked_at=now.time()
            still_locked_at=still_locked_at.strftime("%H:%M:%S")
            
            print("still locked",still_locked_at)
            t11=p.parse(locked_at)
            t22=p.parse(still_locked_at)
            diff=t11-t22
            break_as_of_now=-(diff.seconds)
            print("break_as_of_now",break_as_of_now) #10800 #3hrs
            if break_as_of_now>10800:
                hold_on()
            
            if isLocked()==False:
                now = datetime.datetime.now().replace(microsecond=0)
                unlocked_at=now.time()
                unlocked_at=unlocked_at.strftime("%H:%M:%S")
                print("unlocked_at",unlocked_at)
                print(type(unlocked_at))
                
                t1=p.parse(locked_at)
                print(t1)
                


                t2=p.parse(unlocked_at)
                print(t2)
                diff=t1-t2
                break_time=-(diff.seconds)
                print("break_time",break_time)
                last_break_time=t.strftime('%H:%M:%S', t.gmtime(break_time))
                print("most recent break_time",last_break_time)
                
                if break_time>10800: #more than 3 hours
                    hold_on()
                else:
                    locked_time=locked_time+break_time

                if locked_time>10800:
                    os.system("shutdown -l")
                    
                
                total_locked_time=t.strftime('%H:%M:%S', t.gmtime(locked_time))
                print("locked_time:",total_locked_time)
                

                '''------------------db part----------------------------'''
                
                cnxn=pyodbc.connect('DSN=test3;UID=sa;PWD=your password')
                cursor = cnxn.cursor()
                if break_time<10800:
                    cursor.execute ("UPDATE track_hours SET most_recent_break='%s', total_locked_time='%s' WHERE ID='%d' " % (last_break_time, total_locked_time,record_id))
                else:
                    t.sleep(5)
                    os.system("shutdown -l")
                    t.sleep(2)
                    sys.exit("user taken more 3 hrs break")
                    
                    
                sql1="INSERT INTO raw_tracker_data (user_name, date, login_time,break_start_at,break_end_at,total_break_time) VALUES (?,?,?,?,?,?)"
                val1=(name,today,login_time,locked_at,unlocked_at,last_break_time)
                cursor.execute(sql1,val1)
                cnxn.commit()
                cnxn.close()
                
                


                
                

                
        
    
 
        
        
    
        
        
        

    
