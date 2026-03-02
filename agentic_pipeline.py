from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from rag_pipeline import generate_strict_answer
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    timeout=20
)

query_agent = Agent(
    role="Query Optimization Expert",
    goal="Rewrite the user query clearly for accurate retrieval.",
    backstory="Expert in improving search queries for document systems.",
    llm=llm,
    verbose=False
)

evaluator_agent = Agent(
    role="Answer Quality Controller",
    goal="Ensure answer is document-based and well formatted.",
    backstory="Expert in validating and polishing document-based responses.",
    llm=llm,
    verbose=False
)

def run_agentic_rag(user_query):

    # Step 1: Rewrite query
    rewrite_task = Task(
        description=f"""
Rewrite this question clearly and precisely:

{user_query}

Return only the improved query.
""",
        expected_output="Refined query.",
        agent=query_agent
    )

    crew = Crew(
        agents=[query_agent],
        tasks=[rewrite_task],
        process=Process.sequential,
        verbose=False
    )

    refined_query = crew.kickoff()

    # Step 2: Retrieve from RAG (safe call)
    answer, sources, confidence = generate_strict_answer(str(refined_query))

    # Step 3: Final polishing
    polish_task = Task(
        description=f"""
Polish this answer for clarity and neat formatting:

{answer}

Ensure:
- Clear structure
- 5–10 lines
- No external knowledge
""",
        expected_output="Polished final answer.",
        agent=evaluator_agent
    )

    crew2 = Crew(
        agents=[evaluator_agent],
        tasks=[polish_task],
        process=Process.sequential,
        verbose=False
    )

    final_answer = crew2.kickoff()

    return final_answer, sources, confidence