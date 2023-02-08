numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replace_text_by_num(text: str) -> str:
    """Replace words with their equivalent numbers."""
    number_map: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for k, v in number_map.items():
        text = text.replace(k, v)
    return text


def replace_expressions(text: str) -> str:
    """Replace words with their mathematical equivalents."""

    # Define the text to replace in the text.
    replace_text: dict[str, str] = {
        "plus": "+",
        "minus": "-",
        "over": "/",
        "divided by": "/",
        "divide by": "/",
        "by": "*",
        "divided": "/",
        "divide": "/",
    }

    # Replace the text.
    for word, replacement in replace_text.items():
        text = text.replace(word, replacement)

    # Close the square root.
    if "square root" in text:
        text = text.replace("square root ", "sqrt(") + ")"

    return text


# this code is trying to determine if the string is a math expression or not. 
def is_math_expression(text: str) -> bool:
    """Determine if the string is a math expression or not."""
    calc: bool = False
    for i in text:
        calc = i in numbers
    return calc != False