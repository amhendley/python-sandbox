from borb.pdf.pdf import PDF

# Read PDF
with open("output_001.pdf", "rb") as pdf_file_handle:
    input_pdf_001 = PDF.loads(pdf_file_handle)

# Rotate page
input_pdf_001.get_page(0).rotate_left()

# Write PDF to disk
with open("rotated_output.pdf", "wb") as pdf_out_handle:
    PDF.dumps(pdf_out_handle, input_pdf_001)
