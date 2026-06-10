from memory.history import chat_history

chat_history.add_user_message(
    "My name is Pratiksha"
)

chat_history.add_ai_message(
    "Nice to meet you"
)

for msg in chat_history.messages:
    print(msg)