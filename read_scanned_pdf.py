import os.path
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from datetime import date

class ReadScannedPDF:
    def __init__(self,tesseract_path=None,poppler_path = None):
        self.platform_name = platform.system()
        self.tesseract_path = tesseract_path
        self.poppler_path = poppler_path


    def getText(self,pdf_path):
        self.image_file_list = []
        self.PDF_file = pdf_path
        self.main_string = ""
        
        pytesseract.pytesseract.tesseract_cmd = Path(r"H:\PRODUCTION REPORTS\Business Intelligence\Chromedriver\tesseract.exe")
        if self.poppler_path == None :
            path_to_poppler_exe = Path(r"H:\PRODUCTION REPORTS\Business Intelligence\Chromedriver\poppler-0.68.0\bin")
        else:
            path_to_poppler_exe = Path(self.poppler_path)

        #Here If pdf Path Exist then it extract text             
        if os.path.exists(self.PDF_file):
            print(self.PDF_file)
            with TemporaryDirectory() as tempdir:
                if platform.system() == "Windows":
                    pdf_pages = convert_from_path(self.PDF_file, 500, poppler_path=path_to_poppler_exe)
                else:
                    pdf_pages = convert_from_path(self.PDF_file, 500)

                for page_enumeration, page in enumerate(pdf_pages, start=1):
                    filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
                    page.save(filename, "JPEG")
                    self.image_file_list.append(filename)


                for image_file in self.image_file_list:
                    text = str(((pytesseract.image_to_string(Image.open(image_file)))))
                    text = text.replace("-\n", "")
                    self.main_string = self.main_string + text
            #write text file
            filename = self.PDF_file.replace(".pdf",".txt")
            with open(filename, "w") as f:
                     f.write(self.main_string)
            print("Scanned for file ",self.PDF_file)
        return self.main_string

##pdf_obj = ReadScannedPDF()
##pdf_text = pdf_obj.getText(r"scanned_pdf.pdf")
##print(pdf_text)
