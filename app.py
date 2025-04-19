import app.pdfextract as pe

pages = pe.read_pdf("Culinary Companion.pdf")
print("Total pages: ", len(pages))