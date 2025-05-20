from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_pdf(text, filename):
     c = canvas.Canvas(filename, pagesize=letter)
     text_lines = text.split('\n')
     y = 750
     for line in text_lines:
          c.drawString(40, y, line)
          y -= 15
          if y < 50:
               c.showPage()
               y = 750
     c.save()

def save_word(text, filename):
     doc = Document()
     for para in text.split('\n\n'):
          doc.add_paragraph(para)
     doc.save(filename)