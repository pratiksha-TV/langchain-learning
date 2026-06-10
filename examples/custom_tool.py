from langchain_core.tools import tool

@tool
def add(a: int, b: int):
    """Add numbers"""
    return a + b

@tool
def multiply(a: int, b: int):
    """Multiply numbers"""
    return a * b

print(add.invoke({
    "a": 10,
    "b": 20
}))

print(multiply.invoke({
    "a": 10,
    "b": 20
}))