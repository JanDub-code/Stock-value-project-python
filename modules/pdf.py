from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas

def pdf_gen(ticker, image1, image2, image3, image4, image5, sub_title, before_photos, before_stock, text_output):
    # Definitions of titles ect.
    fileName = 'Python_projekt.pdf'
    documentTitle = 'Stock evaluation'
    title = 'Stock evaluation'
    subTitle = sub_title

    # Birth of the PDF
    pdf = canvas.Canvas("Python_projekt.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    style = styles['Normal']

    # page 1
    # title
    pdf.setFont("Helvetica", 30)
    pdf.drawCentredString(300, 765, title)

    # text
    pdf.setFont("Courier", 14)
    pdf.drawCentredString(300, 720, subTitle)
    text = pdf.beginText(60, 680)
    pdf.setFont("Courier", 12)
    for line in before_photos:
        text.textLine(line)
    pdf.drawText(text)

    # section 1
    pdf.drawImage(image1, 20, 420, 280, 220)
    pdf.drawImage(image2, 300, 420, 280, 220)

    # section 2
    pdf.drawImage(image3, 20, 160, 280, 220)
    pdf.drawImage(image4, 300, 160, 280, 220)

    pdf.showPage()

    # page 2
    pdf.drawImage(image5, 30, 360, 540, 380)
    text = pdf.beginText(95, 760)
    pdf.setFont("Courier", 12)
    for line in before_stock:
        text.textLine(line)
    pdf.drawText(text)
    text = pdf.beginText(110, 320)
    pdf.setFont("Courier", 16)
    for line in text_output:
        text.textLine(line)
    pdf.drawText(text)


    pdf.save()


