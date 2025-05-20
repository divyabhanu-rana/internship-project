from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.app.core.vectorstore import get_relevant_chunks
from backend.app.core.prompt_builder import build_prompt
from backend.app.core.embedding import call_llm  # Import call_llm directly here
from backend.app.utils.formatter import format_output
from backend.app.utils.file_ops import save_pdf, save_docx
from backend.app.models.schema import GenerationRequest, GenerationResponse
import os
import uuid

router = APIRouter()

@router.post("/generate", response_model=GenerationResponse)
def generate_question_paper(req: GenerationRequest):
    try:
        # 1. RETRIEVING RELEVANT CONTENT FROM vector store
        relevant_chunks = get_relevant_chunks(
            grade=req.grade,
            chapter=req.chapter,
            subject=None,
            top_k=10
        )

        # 2. BUILDING THE PROMPT
        prompt = build_prompt(
            context_chunks=relevant_chunks,
            request=req
        )

        # 3. CALLING THE LLM (uses latest version from embedding.py file)
        result = call_llm(prompt, req.type)

        # 4. FORMATTING THE OUTPUT
        formatted = format_output(result, req.type)

        # 5. SAVING THE OUTPUT TO A FILE
        out_id = str(uuid.uuid4())
        pdf_path = os.path.join("exports/pdfs", f"{out_id}.pdf")
        docx_path = os.path.join("exports/word-docs", f"{out_id}.docx")
        save_pdf(formatted, pdf_path)
        save_docx(formatted, docx_path)
        return GenerationResponse(
            paper=formatted,
            pdf_url=f"/exports/pdfs/{out_id}.pdf",
            word_url=f"/exports/docx/{out_id}.docx"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))