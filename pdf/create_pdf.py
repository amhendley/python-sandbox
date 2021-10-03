from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.page_layout.multi_column_layout import \
    SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from decimal import Decimal
import loremipsum


heading_color: HexColor = HexColor("0b3954")
text_color: HexColor = HexColor("de6449")
file_name: str = "output.pdf"
d: Document = Document()

N: int = 10
for i in range(0, N):
    # Create a new Page, and append it to the Document
    p: Page = Page()
    d.append_page(p)

    # Set the PageLayout of the new Page
    l: PageLayout = SingleColumnLayout(p)

    # Add the paragraph to identify the Page
    l.add(Paragraph("Page %d of %d" % (i + 1, N),
                    font_color=heading_color,
                    font_size=Decimal(24)))

    # Add a Paragraph of dummy text
    # l.add(Paragraph("""
    #                 Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    #                 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    #                 when an unknown printer took a galley of type and scrambled it to make a type specimen book.
    #                 It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
    #                 It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
    #                 and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    #                 """,
    #                 font_color=text_color))
    _, _, paragraph_text = loremipsum.generate_paragraph(start_with_lorem=True)

    print(paragraph_text)
    l.add(Paragraph(paragraph_text[:1000], font_color=text_color))

# Persist the Document to disk
with open(file_name, "wb") as pdf_out_handle:
    PDF.dumps(pdf_out_handle, d)
