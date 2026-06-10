from tools.rag_tool import search_knowledge

result = search_knowledge.invoke(
    {
        "question": "What is Spring Boot?"
    }
)

print(result)