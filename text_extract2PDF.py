#code to extract the text from jpg and add that extracted text into new pdf with good style
#script for upwork
import jinja2
import pdfkit
import time
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
image_path = r"C:\Users\prave\Downloads\IMG_20221029_133515_513.jpg"
img = cv2.imread(image_path)
extracted_text=pytesseract.image_to_string(img)
print(extracted_text)
print(type(extracted_text))
text_list=extracted_text.split('\n\n')
print(text_list)
for text in text_list:
    print(text)
    print('***************')

context={
'chapter_name':text_list[0],
'chapter_num':text_list[1].split('\n')[0],
'para_name':text_list[1].split('\n')[-1],
'para_text1':text_list[2],
'para_text2':text_list[3]
}
tempalte_loader=jinja2.FileSystemLoader(r'C:\Users\prave\Desktop\PDF_automation')#folder where html template is
template_env=jinja2.Environment(loader=tempalte_loader)
template=template_env.get_template('mybasic_template.html')
output_text=template.render(context)
exe_path=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config=pdfkit.configuration(wkhtmltopdf=exe_path)
pdfkit.from_string(output_text,'pdf_generated.pdf',configuration=config,css='my_style.css')





