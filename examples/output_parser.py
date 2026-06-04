from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple English"
)

llm = ChatOllama(model="llama3")

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke(
    {"topic": "Kafka"}
)

print(type(result))
print(result)