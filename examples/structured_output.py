from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

class InterviewAnswer(BaseModel):
    definition: str
    example: str
    interview_answer: str

llm = ChatOllama(model="qwen3")

structured_llm = llm.with_structured_output(
    InterviewAnswer
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{question}")
])

chain = prompt | structured_llm

response = chain.invoke({
    "question": "What is Kafka?"
})

print(response)