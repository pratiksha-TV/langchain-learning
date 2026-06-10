from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.

    Example:
    25 + 17
    10 * 5
    """

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"