import csv
import datetime
import json
import os
import sys
import openpyxl
import requests
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha

header = ['product_id', 'city', 'area', 'address', 'area_sqft', 'property_type', 'contact_person_name',
          'ad_posted_date', 'seller_type', 'summary', 'mobile_number', 'email', 'timestamp']

with open('output-3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)

wb = openpyxl.load_workbook('city_codes.xlsx')
sheet = wb.active

# Appending keywords to List
keywords_lists = []
for i in range(2, 102):
    c_cell = sheet[f"B{i}"].value
    if c_cell == 'NA' or c_cell == None:
        continue
    else:
        print(c_cell)
        keywords_lists.append(c_cell)

print(len(keywords_lists))


class Acres:
    def __init__(self, mail, password, city_code):
        self.session = requests.Session()
        self.mail = mail
        self.password = password
        self.city_code = city_code
        self.current_url = f"https://www.99acres.com/search/property/lease/?city={self.city_code}&property_type=91,92&preference=L&area_min=5000&area_unit=1&res_com=C"
        self.session.get('https://www.99acres.com/')

    def citycode(self):
        # add all the city codes in a list and pass it one by one into detail_fetcher and scraper
        self.city_code = []
        pass

    def recaptcha_solver(siteurl):
        sitekey = '6LfEtwsTAAAAAMFkCNFXZfarugQ2UBHIDs1JMrH9'
        apikey = '014fed7631a883958753afbeee0aa267'
        api_key = os.getenv('APIKEY_2CAPTCHA', apikey)

        solver = TwoCaptcha(api_key)

        try:
            result = solver.recaptcha(
                sitekey=sitekey,
                url=siteurl,
                version='v3')

        except Exception as e:
            sys.exit(e)

        else:
            answer = result.get('code')
        return answer

    def login(self):
        url = "https://www.99acres.com/api-aggregator/auth/login"

        headers = {"content-type": "application/json; charset=utf-8", "referer": "https://www.99acres.com/"}
        data_ = f'"userName":"{self.mail}","password":"{self.password}","mode":"LOGIN_PASSWORD","source":"react","sellerPage":false'
        data = '{' + data_ + '}'

        self.session.post(url, headers=headers, data=data)

    def get_details(self):
        url = "https://www.99acres.com/do/buyer/ShowBuyerForms/editBuyerProfile"

        resp = self.session.get(url)
        soup = BeautifulSoup(resp.content, 'html5lib')

        country_code = soup.find('span', id='country_code').get_text().strip()
        self.country_code = ''.join(i for i in country_code if i.isdigit())
        self.phone_no = soup.find('input', id='BMmobile')['value']
        self.name = soup.find('input', id='BMname')['value']
        self.email = soup.find('input', id='BMemail')['value']

    def detail_fetcher(self, product_id):
        url = "https://www.99acres.com/api-aggregator/eoi/doEoi"

        headers = {"content-type": "application/json; charset=utf-8",
                   "referer": self.current_url}

        data_ = f'"name":"{self.name}","email":"{self.email}","countryCode":"{self.country_code}","phone":"{self.phone_no}","query":"I am interested in this project.","identityRatio":"I","productId":"{product_id}","trackSource":"SRP_VIEW_PHONE_FSL_REACT_REVAMP","responseType":"C2V","eoiOn":"PROPERTY","siteVisit":"Yes","visitorId":"5690111651215937586","page":"SRP","platform":"Desktop"'
        data = '{' + data_ + '}'

        resp = self.session.post(url, headers=headers, data=data)
        response = json.loads(resp.content)
        # print(response)
        mobile = 'Not available'
        email_id = 'Not available'

        try:
            details = response['sellerResponseDetails'][0]
            mobile = details['mobile']
            email_id = details['email']
        except KeyError:
            pass
        return mobile, email_id

    def scraper(self):
        e_input = self.encrypted_input()
        url = f"https://www.99acres.com/api-aggregator/discovery/srp/search?page=1&page_size=1000&platform=DESKTOP&encrypted_input={e_input}&search_type=QS"

        headers = {
            "referer": self.current_url}

        resp = requests.get(url, headers=headers)
        response = json.loads(resp.content)
        property_ = response['properties']
        print(len(property_))

        for properties in property_:
            product_id = properties['PROP_ID']
            metadata = properties['location']
            city = metadata['CITY_NAME']
            area = metadata['LOCALITY_NAME']
            try:
                address = metadata['ADDRESS']
            except:
                address = 'NA'

            area_sqft = properties['AREA']
            property_type = properties['PROPERTY_TYPE']
            contact_person_name = properties['CONTACT_NAME']
            ad_posted_date = properties['REGISTER_DATE']
            seller_type = properties['CLASS_LABEL']
            summary = properties['DESCRIPTION']
            mobile, email = self.detail_fetcher(product_id)
            timestamp = datetime.datetime.now()

            row_ = [product_id, city, area, address, area_sqft, property_type, contact_person_name, ad_posted_date,
                    seller_type, summary, mobile, email, timestamp]

            with open('output-3.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row_)

    def encrypted_input(self):
        url = f'https://www.99acres.com/api-aggregator/discovery/srp/search?property_type=91%2C92&area_min=5000&area_unit=1&platform=DESKTOP&moduleName=GRAILS_SRP&workflow=GRAILS_SRP&page_size=25&page=1&commercial_category=OS&city={self.city_code}&preference=L&res_com=C&seoUrlType=DEFAULT'
        headers = {'authority': 'www.99acres.com',
                   'referer': f'{self.current_url}'}

        data = {'property_type': '91,92',
                'area_min': '5000',
                'area_unit': '1',
                'platform': 'DESKTOP',
                'moduleName': 'GRAILS_SRP',
                'workflow': 'GRAILS_SRP',
                'page_size': 25,
                'page': 1}
        response = requests.get(url, data=data, headers=headers)
        json_data = json.loads(response.text)
        # print(json_data)
        encrypted_inpt = json_data['encrypted_input']
        print(f"{self.city_code}:{encrypted_inpt}")
        return encrypted_inpt


username = 'dollie2606@gmail.com'
password = 'Dollie@123'

for i in range(len(keywords_lists)):
    object = Acres(username, password, keywords_lists[i])
    object.login()
    object.get_details()
    object.scraper()
    # object.encrypted_input()
    print(f"Done with: {keywords_lists[i]}")
