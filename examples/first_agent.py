from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a math expression.
    Example: 25 + 17
    """
    return str(eval(expression))


@tool
def get_weather(city: str) -> str:
    """
    Get weather for a city.
    """
    return f"Weather in {city} is 28°C and sunny."


@tool
def java_knowledge(question: str) -> str:
    """
    Answer Java interview questions.
    """
    return "Spring Boot is a framework used to build Java applications."

llm = ChatOllama(
    model="qwen3",
    think=False,  # disable thinking mode for tool calling
)

tools = [calculator, get_weather, java_knowledge]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

response = agent_executor.invoke({"input": "what is my name?"})
print(response)
