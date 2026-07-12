import os
from crewai import Agent, Task, Crew, Process, LLM

# Set Ollama API endpoint (you can change this if needed)
OMLX_HOST = "http://127.0.0.1:4000/v1"

# Configure the LLM using CrewAI's LLM class (pointing to local instance)
llm = LLM(
    model="openai/Qwen3-4B-Instruct-2507-4bit",  # Prefix with openai/ to use OpenAI compatible API
    base_url=OMLX_HOST,
    api_key="not-needed",
    temperature=0.2,
)

# Define the agents
researcher = Agent(
    role='Researcher',
    goal='Find the latest research papers on climate change impacts',
    backstory='A seasoned researcher with deep knowledge in environmental science',
    memory=True,
    llm=llm,
    allow_delegation=True,
)

writer = Agent(
    role='Writer',
    goal='Write a concise summary of the research findings in a clear and engaging way',
    backstory='A skilled writer who can translate complex scientific content into accessible language',
    llm=llm,
    memory=True,
    allow_delegation=True,
)

summarizer = Agent(
    role='Summarizer',
    goal='Summarize the key points from the research and writing output',
    backstory='An expert in concise summarization and content compression',
    llm=llm,
    memory=True,
    allow_delegation=True,
)

# Define tasks
research_task = Task(
    description="Search and summarize recent climate change research papers from 2023–2024",
    agent=researcher,
    expected_output="List of 5 relevant research papers with links and key findings.",
)

writer_task = Task(
    description="Take the research findings and write a 200-word summary for a general audience",
    agent=writer,
    expected_output="A clear, engaging summary of climate change impacts in simple language.",
)

summerizer_task = Task(
    description="Extract the key points from the writer's output and create a one-paragraph summary",
    agent=summarizer,
    expected_output="A concise 50-word summary of the main findings.",
)

# Create the crew with a sequential process
crew = Crew(
    agents=[researcher, writer, summarizer],
    tasks=[research_task, writer_task, summerizer_task],
    process=Process.hierarchical,  # or Process.sequential
    manager_llm=llm,
    verbose=True,  # Print the full conversation
)

# Execute the crew
result = crew.kickoff()

# Print final output
print("\n" + "="*60)
print("FINAL OUTPUT:")
print("="*60)
for i, task in enumerate(crew.tasks):
    print(f"\nTask {i+1}: {task.description}")
    print("Output:", task.output.raw if hasattr(task, 'output') and hasattr(task.output, 'raw') else "N/A")
print("\n" + "="*60)
