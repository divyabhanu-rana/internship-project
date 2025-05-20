import os
from transformers import AutoTokenizer, AutoModelForCasualLM

_tokenizer = None
_model = None

def get_model_and_tokenizer():
     global _tokenizer, _model
     if _tokenizer is None or _model is None:
          model_path = os.getenv("DEEPSEEK_MODEL_PATH", r"")
          _tokenizer = AutoTokenizer.from_pretrained(model_path)
          _model = AutoModelForCasualLM.from_pretrained(model_path)
     
     return _model, _tokenizer