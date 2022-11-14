with pdfplumber.open("example.pdf") as pdf:
    for page in pdf.pages:
        page.extract_text()
