from borb.pdf.document import Document
from borb.pdf.pdf import PDF


# Read first PDF
with open("output_001.pdf", "rb") as pdf_file_handle:
    input_pdf_001 = PDF.loads(pdf_file_handle)

# Read second PDF
with open("output_002.pdf", "rb") as pdf_file_handle:
    input_pdf_002 = PDF.loads(pdf_file_handle)

# Build new PDF by concatenating two inputs
output_document = Document()
output_document.append_document(input_pdf_001)
output_document.append_document(input_pdf_002)

# Write PDF
with open("combined_output.pdf", "wb") as pdf_out_handle:
    PDF.dumps(pdf_out_handle, output_document)
