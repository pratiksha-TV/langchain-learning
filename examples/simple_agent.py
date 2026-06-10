from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def add(a: int, b: int):
    """Add two numbers"""
    return a + b

llm = ChatOllama(
    model="qwen3"
)

tools = [add]

llm_with_tools = llm.bind_tools(tools)

response = llm_with_tools.invoke(
    "What is 25 + 17?"
)

print(response)