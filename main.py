from crewai_file import run_email_crew
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    inputs = {
        "recipient": "HR Manager",
        "purpose": "introducing myself and expressing interest in open AI Engineering roles"
    }

    run_email_crew(inputs)
