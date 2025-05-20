import fitz

def extract_text_from_pdf(pdf_path):
     doc = fitz.open(pdf_path)
     text = ""
     for page in doc:
          text += page.get_text()
     return text

def extract_sections_by_chapter(pdf_path, chapter_names):
     """Extract text chunks from a PDF based on specified chapter names."""
     text = extract_text_from_pdf(pdf_path)
     results = {}
     for chapter in chapter_names:
          idx = text.lower().find(chapter.lower())
          if idx != -1:
               results[chapter] = text[idx:idx + 4000]  # Extract 4000 characters after the chapter name
     return results