from langchain_ollama import ChatOllama

from tools.calculator import calculator
from tools.weather import get_weather
from tools.rag_tool import search_knowledge
from tools.current_time import current_time
from utils.safe_execution import safe_tool_execution

from memory.history import chat_history


llm = ChatOllama(
    model="qwen3"
)

tools = [
    calculator,
    get_weather,
    search_knowledge,
    current_time
]

llm_with_tools = llm.bind_tools(tools)

tool_map = {
    "calculator": calculator,
    "get_weather": get_weather,
    "search_knowledge": search_knowledge,
    "current_time": current_time
}


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    chat_history.add_user_message(user_input)

    response = llm_with_tools.invoke(
        chat_history.messages
    )

    if response.tool_calls:

        tool_results = []

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]

            args = tool_call["args"]

            selected_tool = tool_map.get(tool_name)

            if not selected_tool:
                continue

            result = safe_tool_execution(
    selected_tool,
    args
)

            tool_results.append(
                f"{tool_name}: {result}"
            )

        tool_context = "\n".join(tool_results)

        final_response = llm.invoke(
            f"""
User Question:
{user_input}

Tool Results:
{tool_context}

Create a helpful answer using the tool results.
"""
        )

        print("\nAI:")
        print(final_response.content)

    else:

        print("\nAI:")
        print(response.content)