
from fastapi import FastAPI, UploadFile, Form
from matching import match_resume_to_job
from utils import extract_text_from_pdf

app = FastAPI()

@app.post("/match")
async def match(resume: UploadFile, job_description: str = Form(...)):
    if resume.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(await resume.read())
    else:
        resume_text = (await resume.read()).decode("utf-8")
    
    score = match_resume_to_job(resume_text, job_description)
    return {"match_score": round(score * 100, 2)}
