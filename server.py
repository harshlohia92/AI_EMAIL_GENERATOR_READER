from fastapi import FastAPI
from crewai_file import run_email_crew

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Mail Agent API is live on Render 🚀"}

@app.post("/run-email-agent/")
def run_email_agent(inputs: dict):
    result = run_email_crew(inputs)
    return {"message": "Task completed successfully", "result": result}
