from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests,sys
import time
def get_doc_data(url):
    page=requests.get(url)
    # print(page)
    soup=BeautifulSoup(page.text,'lxml')
    # print(type(soup))
    # print(soup.text)
    # print(soup.prettify())
    # print('==============================================')
    inner_class_data=soup.find('div',class_='inner')
    # print(inner_class_data)
    full_name=inner_class_data.find('b')
    # print(full_name)
    # print(type(full_name))
    full_name=full_name.text
    list1=inner_class_data.find_all('span')
    # print(list1)
    gender=list1[0].text
    try:
        speciality=list1[1].text
    except:
        speciality='NA'
    try:
        city_state=list1[2].text
    except:
        city_state='NA' 
    # print(gender,speciality,city_state)
    practice_loc_data=soup.find('div',class_='LocationsDetails__Wrapper-sc-1pryox8-0 ktSsqK')
    # print(practice_loc_data)
    try:
        pract_hospital=practice_loc_data.find('h5').text
    except:
        pract_hospital='NA'
    # print(pract_hospital)
    try:
        pract_add=practice_loc_data.find('span').text
    except:
        pract_add=''
    # print(pract_add)
    try:
        phone_data=practice_loc_data.find_all('div',class_='item')[2].text
    except:
        phone_data='NA'
    # print(phone_data)
    time.sleep(2)
    return full_name,gender,speciality,pract_hospital,pract_add,city_state,phone_data

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# # to supress the error messages/logs
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\prave\Desktop\chromedriver.exe')
# driver.get('https://intake.steerhealth.io/doctor-search/aa1f8845b2eb62a957004eb491bb8ba70a')

# SCROLL_PAUSE_TIME = 4

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# time.sleep(5)

# soup = BeautifulSoup(driver.page_source, 'lxml')
# docs_list=soup.find_all('div',class_="btnsWrapper")
# print(docs_list)
# print(len(docs_list))
# doc_url_list=[]
# for i in docs_list:
#     each_doc_link=i.find('a').get('href')
#     print(each_doc_link)
#     doc_url="https://intake.steerhealth.io"+each_doc_link
#     doc_url_list.append(doc_url)
# print(doc_url_list)
doc_url_list=['https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bc48c646acf87589612337aa83b7bad508', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cb5ac97987f269ac550469af94ee98ea27', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c84790659dc548af46375b9eb3e3bdf91a', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c7159d4f9ee942f12b0661b48db99ad921', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9467b46599ef7e8624246eb3d6b78faa19', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8647b557b0c2758e507e75b7b49189d93c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c84ccd7995c81ffa77327aa98f88affa67', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c71eac4fce924da7712e4fa48eaaadfe3a', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/945e8b7891cb4285611465aaa7bde3d83d', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/aa5abc079bd261876202719991a2e3a165', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b35b97749eec12a6400034e499a9a9a502', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/94558b79accb6998450d308fa8a8e3a724', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/885caa7b94987f916b2a5796a6abb9e731', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ba75944e9ecc45af782364e996b1accb3b', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8e6e904ba49f5fa7732352a9938ae8c017', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8e18876e9dfb4986542f5bbcb4e8bec722', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/af159d6db3ce54f75c2d49aaa2b8bdca05', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/87458e72c2f061f448716ebf82aaa1c067', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/84489877bbc265fb5803408a8398b4a73b', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/87478a49cec266f7787e4dbfadb5a1e01e', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cb79995e9e9d619361336d8a979b9ffd27', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9b759807a5dc628c683153b5aea0b3fa18', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c75f984c83c249ab457e34bea692b0e524', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9b69c7458ee7428f50064990d5bca9d431', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bf449b48b59d40b350174793d5b49fab61', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c87fac50a2df61a37974659891b9a9f231', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cc63906fbbf36ffa58317793919095fd17', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cb43a46bcff86484713d799cd8adb8f934', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bd6ba906bb924a8f601357b9a5e8a1e239', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c645bf6cbec7138f45017590908eb1e423', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bc7e8465afe2529043256991acaba2f618', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/994ebf66cfdf1ef1670246a8bae89ade16', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9a7797659cf36dad2b0b72bfb0efacfb3b', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/af5db949c3f94ca540293b96ade3adfd37', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c6638d51b4dc13ad7b0a7aea81b1ecd021', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8d67a70bbe9f40852673539788eeb2cb21', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ac429a0998c164a52633769e8290bafa33', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ac5da472b0c945f7241d62bad3b8adf915', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9b40890d90fd14f7770941e8a5a883e31c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ba5eca6d8fee62b62072478a899dece727', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a740b45a9cd91e8c7d0450b99794b3f210', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/aa4f8b5993c84f80501575acd6ef95df23', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cd4fb04b98fe6fbb5a2a48ae87b499fd03', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c95abd0acefd42b7583e7bafb4ad9fd818', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cd60a46b99f256956516678589a2bcf23f', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a946bd6c85cc60a4792651a58e9eb5f025', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bb46cb5e99cc4f935c1e3bb0ab92a2ab37', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/936998458ef87098670166afa791b9d66a', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bf158b4f9cd04c95540460b094e8b4c020', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a91e947980984d89553366a991efbeaa60', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8f54b978b5f05db24b2e44a9878891fa39', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/845e9b5aa4e743fa610f729ed49cb0de61', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b3548c73999f51f7780041978aeebcc464', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b85d9145cee64386730d31b7d9afedea39', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9c158c7a86cd6da3463e72e993b583e527', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bf5d940a90ec5e89242a6cac8d889ae608', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/aa189859b0d311a86b2d6ee9d6b4ecd811', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/987cc77bb5e446a17332469789b4b4c966', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a414874ccecd43ab423e65e8ace99afb37', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/994eb806829e4a8542313bacd7aba9d560', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a45ab80882e864b72700739e82abafc365', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/944fc9079b9976b863017abf92bd9fc93c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8b75b60990de74a8772249aba8bf91ca02', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b463910798f25491640f67b7a4a3a1f614', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/874f980ba1c962886720539193ed89d628', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8c18c855bcf01ea845257bb395b4b9de25', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ba75945bbaf845a6557e42aed38088e503', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8b6fa64bc0e84ff7402d3b8f8eb189fb65', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b84ac658a6e65e93790f6eb0ace8bedb3f', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/995ab65cb8d36bb7590535aeaab8afd724', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9a69905a82f37687452a31adbabcb8f837', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8c4cb65ca6dc15b5482947ada8afb5d960', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b9428e6ecfc2698a58135184d8b0e9a024', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b94ccc08c3d05eaf611075b5a2ad83dd0a', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9779c7478cc769814626688a88bbbee223', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9565b84fb3c714925105379793ab8fdd15', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/88409f49bee762af7b7352a7a69882ab06', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9140a44799fa75bb781f70a9b0bc99dd33', 'https://intake.steerhealth.io/provider/b849b05095c3419325756e8aa6aa9de920/997e8a68b3f95780662f578783aa8ae739', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c6668f5795c5548a59024887d6beb0e300', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cb79946897d975bb5c2154b287b48fc03d', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c665ae0890c8549a742040bbd8b79dc760', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c81a964cbdcc69af5a0f6a849394bda611', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a968b85caef06595660236908b89eefb06', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9344896684e91fa0462f7b9eb9b2bff73b', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/aa58b008ace4438555354bbfa3b5bed21c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8a4293658c9954b7780d64ad96a090dd1f', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9969b80cb8c063957c7248e591abafca3c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/88659867b0f27d936b1f4998a8bfb5a538', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8b189359b4c245a4531647e4a7b5a3e760', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9740c96eacf34cfa7b3673a9d29197eb2b', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ae4a8e4fb3996fab632c7496d8b193a722', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/a67da765c1cd77937b0d5291b1ae9cdd3d', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9761a44cb3dd54f0741673ae85e389de33', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b946a40b99e75faf561d308d8e91eed425', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9d57990b91e46bf426013b91989b8adb3c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c96abb738ee11081557f69978de29aea1e', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c968bd6b99ef13a75932678e87ada8d521', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b640cb0cbae94eba4801689782809ee611', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/c86c874f99cc11fa553077e8d5a3a8f02a', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/847eb248b39c148f753e30acd5b3b3f222', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/8d67ae7cbec712a36220548796acbade61', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/af598e4bc1fd74f446006c9ad4a2e3c724', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/847d9779aed070986a0f46ee8782ede423', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/aa46c97cc59e6cf17606689b9ab4eee414', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b87dc60bc2ed6286451360a483bf98aa38', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/905a9d7bb2e064ba601569b3a89cb5cb61', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/ac4c9a759393119a647537e4b382e2f43f', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/9d558e759ff27fa940224893d4bbecc01c', 'https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/bd61cc7c90da4d8f662a7789888299e566']
df= pd.DataFrame({'Full_name':[''], 'gender':[''], 'speciality':[''], 'Added_speciality':[''],'practice_hospital':[''],'Practice hospital address':[''],'city state zip':[''],'phone':['']})

for url in doc_url_list:
    doctor_info=get_doc_data(url)
    print(doctor_info)
    doctor_info=list(doctor_info)
    df = df.append({'Full_name':doctor_info[0].replace('\xa0',''), 'gender':doctor_info[1],'speciality':doctor_info[2], 'Added_speciality':doctor_info[3],'practice_hospital':doctor_info[4],'Practice hospital address':doctor_info[5],'city state zip':doctor_info[-2],'phone':doctor_info[-1]},
                       ignore_index = True)
    print(type(doctor_info))
    
# df2 = {'Name': 'Amy', 'Maths': 89, 'Science': 93}
# df = df.append(df2, ignore_index = True)
    

    
    df.to_csv(r'C:\Users\prave\Desktop\steerhealth_task\steerhealth_2.csv')
print(df)
    












# #Inputs a job title into the input box
# input_box = driver.find_element_by_xpath('//*[@id="text-input-what"]')
# input_box.send_keys('data analyst')

# #Clicks on the search button
# button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').click()

# #Creates a dataframe
# df = pd.DataFrame({'Link':[''], 'Job Title':[''], 'Company':[''], 'Location':[''],'Salary':[''], 'Date':['']})

# #This loop goes through every page and grabs all the details of each posting
# #Loop will only end when there are no more pages to go through
# while True:  
#     #Imports the HTML of the current page into python
#     soup = BeautifulSoup(driver.page_source, 'lxml')
    
#     #Grabs the HTML of each posting
#     postings = soup.find_all('div', class_ = 'jobsearch-SerpJobCard unifiedRow row result clickcard')
    
#     #grabs all the details for each posting and adds it as a row to the dataframe
#     for post in postings:
#         link = post.find('a', class_ = 'jobtitle turnstileLink').get('href')
#         link_full = 'https://ca.indeed.com'+link
#         name = post.find('h2', class_ = 'title').text.strip()
#         company = post.find('span', class_ = 'company').text.strip()
#         try:
#             location = post.find('div', class_ = 'location accessible-contrast-color-location').text.strip()
#         except:
#             location = 'N/A'
#         date = post.find('span', class_ = 'date').text.strip()
#         try:
#             salary = post.find('span', class_ = 'salaryText').text.strip()
#         except:
#             salary = 'N/A'
#         df = df.append({'Link':link_full, 'Job Title':name, 'Company':company, 'Location':location,'Salary':salary, 'Date':date},
#                        ignore_index = True)
    
#     #checks if there is a button to go to the next page, and if not will stop the loop
#     try:
#         button = soup.find('a', attrs = {'aria-label': 'Next'}).get('href')
#         driver.get('https://ca.indeed.com'+button)
#     except:
#         break

