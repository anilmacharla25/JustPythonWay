import win32api,os,sys
import win32com.client as win32
fname = "C:\\Users\\uname\\Downloads\\Claim Status Detail Report with note.xls"
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fname)

wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
wb.Close()                               #FileFormat = 56 is for .xls extension
excel.Application.Quit()
print("converted to xlsx from xls")



