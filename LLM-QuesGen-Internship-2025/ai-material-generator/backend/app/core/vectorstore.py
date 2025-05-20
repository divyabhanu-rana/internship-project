import faiss
import numpy as np
import os 
import json

VECTOR_DIM = 384

def get_vector_index_path(grade):
     return f"backend/data/{grade}_faiss.index"

def get_metadata_path(grade):
     return f"backend/data/{grade}_chunks.json"

def get_relevant_chunks(grade, chapter, subject=None, top_k=10):
     index_path = get_vector_index_path(grade)
     meta_path = get_metadata_path(grade)

     if not os.path.exists(index_path) or not os.path.exists(meta_path):
          raise ValueError("Vectorstore or metadata missing for this grade.")
     
     index = faiss.read_index(index_path)
     with open(meta_path, 'r') as f:
          chunks = json.load(f)

     from backend.app.core.embedding import get_embedding_model
     embedder = get_embedding_model()
     query_embd = embedder.encode([chapter])
     D, I = index.search(np.array([query_embd]), top_k)
     results = [chunks[i] for i in I[0]]

     return results