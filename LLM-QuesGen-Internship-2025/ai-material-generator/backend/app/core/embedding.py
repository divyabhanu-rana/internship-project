from sentence_transformers import SentenceTransformer
import numpy as np
import torch
from backend.app.core.model_loader import get_model_and_tokenizer

def get_embedding_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(texts):
    model = get_embedding_model()
    return model.encode(texts)

def call_llm(prompt, material_type, max_new_tokens=512, temperature=0.6):
    model, tokenizer = get_model_and_tokenizer()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            pad_token_id=tokenizer.eos_token_id
        )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    # Optionally, keep only generated text:
    return decoded.replace(prompt, "").strip()