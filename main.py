from langchain_ollama import ChatOllama

from tools.calculator import calculator
from tools.weather import get_weather
from tools.rag_tool import search_knowledge

from memory.history import chat_history


llm = ChatOllama(
    model="qwen3"
)

tools = [
    calculator,
    get_weather,
    search_knowledge
]

llm_with_tools = llm.bind_tools(
    tools
)


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    chat_history.add_user_message(
        user_input
    )

    response = llm_with_tools.invoke(
        chat_history.messages
    )

    if response.tool_calls:

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]

            args = tool_call["args"]

            selected_tool = {
                "calculator": calculator,
                "get_weather": get_weather,
                "search_knowledge": search_knowledge
            }[tool_name]

            result = selected_tool.invoke(
                args
            )

            print("\nTool Result:")
            print(result)

    else:

        print("\nAI:")
        print(response.content)