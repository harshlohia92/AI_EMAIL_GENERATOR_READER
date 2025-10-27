from fastapi import FastAPI
from pydantic import BaseModel
from crewai_file import run_email_crew


app = FastAPI(title="AI Email Agent API", version="1.0")

class EmailRequest(BaseModel):
    recipient: str
    purpose: str

@app.get("/harsh")
def home():
    return {"message": "🚀 AI Email Agent API is running!"}

@app.post("/run-email-agent/")
def run_agent(request: EmailRequest):
    inputs = {"recipient": request.recipient, "purpose": request.purpose}
    result = run_email_crew(inputs)
    return {"message": "Task completed successfully", "result": str(result)}