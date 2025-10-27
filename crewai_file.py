from dotenv import load_dotenv
load_dotenv()
from crewai import LLM
from crewai import Agent, Task, Crew
from gmail_connector import read_emails

llm = LLM(

    model="gemini/gemini-2.0-flash",
    temperature=0.5
)

email_agent = Agent(
    role="AI EMAIL MANAGER",
    goal="Write and analyze emails using Gmail. Maintain professionalism and efficiency.",
    backstory=(
        "An AI Email Manager who writes well-structured, polite emails and "
        "monitors unread messages for summaries, spam, and priority classification."
    ),
    verbose=False,
    llm=llm,
)


write_task = Task(
    name="write_task",
    description="Write a professional email to {recipient} about {purpose}. Keep tone polite, concise, and formal.",
    expected_output="A professional email body text.",
    agent=email_agent,
)


read_task = Task(
    name="read_task",
    description="Fetch the latest 5 unread emails from Gmail inbox and summarize them clearly.",
    expected_output="Summary of unread emails.",
    agent=email_agent,
)


spam_task = Task(
    name="spam_task",
    description="Analyze unread emails and classify each as spam or not spam based on the content.",
    expected_output="List of emails with spam/not spam label.",
    agent=email_agent,
)


auto_reply_task = Task(
    name="auto_reply_task",
    description=(
        "Check latest unread emails. If an email is from HR or contains words like "
        "'interview', 'meeting', or 'urgent', generate a polite auto-reply confirming receipt."
    ),
    expected_output="List of emails that would receive an auto-reply with short summaries.",
    agent=email_agent,
)


priority_task = Task(
    name="priority_task",
    description=(
        "Analyze unread emails and classify each as 'High Priority', 'Medium Priority', or 'Low Priority' "
        "based on content and subject."
    ),
    expected_output="List of unread emails with assigned priority levels.",
    agent=email_agent,
)


crew = Crew(
    agents=[email_agent],
    tasks=[write_task, read_task, spam_task, auto_reply_task, priority_task],
    verbose=True,
)



def run_email_crew(inputs):
    print("🚀 Starting AI Email Crew...\n")
    result = crew.kickoff(inputs=inputs)

    print("\n✅ Crew Execution Completed Successfully!\n")
    for task_output in result.tasks_output:
        print(f"\n📋 Task: {task_output.name}")
        print(f"🧠 Agent: {task_output.agent}")
        output_value = getattr(task_output, "output", None) or getattr(task_output, "result", None) or str(task_output)
        print(f"📝 Output: {output_value}")


    print("\n📨 Fetching Inbox Summary...")
    inbox = read_emails()
    if inbox:
        for i, mail in enumerate(inbox, 1):
            print(f"{i}. {mail['subject']} — {mail['snippet']}")
    else:
        print("No emails found.")

    print("\n✅ AI Email Crew finished successfully!")
    return result
