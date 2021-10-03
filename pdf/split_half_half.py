from borb.pdf.document import Document
from borb.pdf.pdf import PDF

# Read PDF
with open("output.pdf", "rb") as pdf_file_handle:
    input_pdf = PDF.loads(pdf_file_handle)

# Create two empty PDFs to hold each half of the split
output_pdf_001 = Document()
output_pdf_002 = Document()

# Split
for i in range(0, 10):
    if i < 5:
        output_pdf_001.append_page(input_pdf.get_page(i))
    else:
        output_pdf_002.append_page(input_pdf.get_page(i))

# Write PDF
with open("output_001.pdf", "wb") as pdf_out_handle:
    PDF.dumps(pdf_out_handle, output_pdf_001)

# Write PDF
with open("output_002.pdf", "wb") as pdf_out_handle:
    PDF.dumps(pdf_out_handle, output_pdf_002)