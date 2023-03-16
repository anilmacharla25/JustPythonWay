#generating pdfs using jinja templating python
import pandas as pd
from reportlab.pdfgen import canvas
from jinja2 import Template

# Read data from Excel file
df = pd.read_excel('data.xlsx')

# Define PDF template using ReportLab
pdf_template = canvas.Canvas('output.pdf')
pdf_template.drawString(100, 750, "{{ name }}")
pdf_template.drawString(100, 700, "{{ address }}")

# Define Jinja template using the PDF template
jinja_template = Template(pdf_template.getpdfdata().decode('utf-8'))

# Generate PDFs for each row of data
for index, row in df.iterrows():
    pdf_data = jinja_template.render(name=row['Name'], address=row['Address'])
    with open(f'{row["Name"]}.pdf', 'wb') as f:
        f.write(pdf_data)
