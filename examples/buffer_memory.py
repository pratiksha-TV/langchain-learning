from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

history = InMemoryChatMessageHistory()

history.add_message(
    HumanMessage(content="My name is Pratiksha")
)

history.add_message(
    AIMessage(content="Nice to meet you")
)

history.add_message(
    HumanMessage(content="I know Java")
)

for message in history.messages:
    print(message)