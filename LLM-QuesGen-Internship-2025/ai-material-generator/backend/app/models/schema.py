from pydantic import BaseModel

class GenerationRequest(BaseModel):
     grade: str
     chapter: str
     type: str # DEFINES WORKSHEET OR QUES PAPER
     difficulty: str

class GenerationResponse(BaseModel):
     paper: str
     pdf_url: str
     word_url: str