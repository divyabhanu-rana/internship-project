import os
import json
from backend.app.core.extraction import extract_text_from_pdf
from backend.app.core.chunking import chunk_text
from backend.app.core.embedding import get_embedding_model
import faiss
import numpy as np

PDF_ROOT = "path/to/pdf/books" # Update this path to your PDF books directory

def process_pdf(pdf_path, grade, subject):
     text = extract_text_from_pdf(pdf_path)
     chunks = chunk_text(text)
     model = get_embedding_model()
     embeddings = model.encode(chunks)
     return chunks, embeddings

def main():
     grades = ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"]
     subjects = ["EVS", "English", "Computer Science"]
     for grade in grades:
          for subject in subjects:
               pdf_file: os.path.join(PDF_ROOT, grade, f"{subject}.pdf")
               if not os.path.exists(pdf_file):
                    continue
               print(f"Ingesting: {pdf_file}")
               chunks, embeddings = process_pdf(pdf_file, grade, subject)
               if len(chunks) == 0:
                    continue
               index = faiss.IndexFlatL2(embeddings.shape[1])
               index.add(np.array(embeddings))
               os.makedirs("backend/data", exist_ok = True)
               faiss.write_index(index, f"backend/data/{grade}_faiss.index")
               with open(f"backend/data/{grade}_chunks.json", "w") as f:
                    json.dump(chunks, f)
               print(f"Finished ingesting {grade}-{subject} PDF.")

if __name__ == "__main__":
     main()