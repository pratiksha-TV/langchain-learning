from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple English"
)

result = prompt.invoke({
    "topic": "Kafka"
})

print(result)