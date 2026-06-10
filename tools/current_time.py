from datetime import datetime
from langchain_core.tools import tool


@tool
def current_time() -> str:
    """
    Returns current time.
    """

    return datetime.now().strftime("%H:%M:%S")