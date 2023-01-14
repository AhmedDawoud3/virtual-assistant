numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replace_text_by_num(text):
    text = text.replace("one", "1")
    text = text.replace("two", "2")
    text = text.replace("three", "3")
    text = text.replace("four", "4")
    text = text.replace("five", "5")
    text = text.replace("six", "6")
    text = text.replace("seven", "7")
    text = text.replace("eight", "8")
    text = text.replace("nine", "9")
    return text


def replace_expressions(text):
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("over", "/")
    text = text.replace("divided by", "/")
    text = text.replace("divide by", "/")
    text = text.replace("by", "*")
    text = text.replace("divided", "/")
    text = text.replace("divide", "/")
    if "square root" in text:
        text = text.replace("square root ", "sqrt(") + ")"

    return text


def is_math_expression(text):
    for i in text:
        calc = True if i in numbers else False
    if calc == False:
        return False
    else:
        return True
