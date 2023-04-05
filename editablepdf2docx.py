from pdf2docx import parse

# Specify the input and output file paths
input_path =r"H:\AR PRODUCTION REPORTS\Business Intelligence\ALL BOTS-NATH\AR\Client\OTG_862\Molina healthcare of SC Auth applied\PriorAuthorizationRequestForm.pdf"
output_path = r"C:\Users\AMacharla\Documents\HEALTHPAC\output.docx"

# Convert the PDF to a Word document
parse(input_path, output_path)
print('done')
