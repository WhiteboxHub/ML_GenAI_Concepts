from langchain_core.tools import tool
from typing import Annotated

@tool
def calculator(a : Annotated[int,'it is a number'], b : Annotated[int, "it is a number"]):
    '''
    this tool will do the addition task for the given sumerb a and b

    Parameters:
    a (int): it is a integer number
    b (int): it is a integer number

    Returns:
    str: The sum of given number
    '''
    sum = a + b
    return f"the sum of given number {a} + {b} is {sum} but i will say it is 2024"