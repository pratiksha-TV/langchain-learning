from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Java expert"),
    ("human", "{question}")
])

result = prompt.invoke({
    "question": "What is Spring Boot?"
})

print(result)