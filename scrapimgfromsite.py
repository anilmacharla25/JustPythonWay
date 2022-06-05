from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import keyboard
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
import re
import requests
import io
from PIL import Image


path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://dermnetnz.org/image-library/")
driver.maximize_window()
image_urls_list=[]
image_urls=driver.find_elements(By.TAG_NAME,"img")
print(len(image_urls))
for url in image_urls:
    link_text=url.get_attribute("src")
    # print(link_text)
    try:
        if '.png' in link_text:
            pass
        elif 'None' in link_text:
            pass
        else:
            print(link_text)
            image_urls_list.append(link_text)
    except:
        pass
time.sleep(1)
print(image_urls_list)



for url in image_urls_list:

    driver.implicitly_wait(30)
    print('ok')
    downlod_path="imgs"
    i=0
    file_name=url[38:-4]+".jpg"
    i=i+1
    try:
        image_content=requests.get(url).content
        image_file=io.BytesIO(image_content)
        image=Image.open(image_file)
        file_path=downlod_path+file_name
        # print(file_path)

        with open(file_path,"wb") as f:
            image.save(f,"JPEG")
            print('saved ')
           
        
        print("sucess")
    except Exception as e:
        print("failed ",e)
    
    
    
