import math
hour_found = False
minute_found = False


def replace_theTexting_by_num(theText):
    theText = theText.replace("one", "1")
    theText = theText.replace("two", "2")
    theText = theText.replace("three", "3")
    theText = theText.replace("four", "4")
    theText = theText.replace("five", "5")
    theText = theText.replace("six", "6")
    theText = theText.replace("seven", "7")
    theText = theText.replace("eight", "8")
    theText = theText.replace("nine", "9")
    return theText


def replace_expresions(MyText):
    MyText = MyText.replace("by", "*")
    MyText = MyText.replace("divide", "/")
    MyText = MyText.replace("divided by", "/")
    MyText = MyText.replace("over", "/")
    MyText = MyText.replace("square root ", "sqrt(") + ")"

    return MyText


def get_hours(text):
    global hour_found
    h = 0
    for i in range(len(text)):
        if str(text[i: i+4]) == "hour":
            hour_found = True
            h = i
            break

    i = 0
    if hour_found == True:
        for i in range(h, 0, -1):
            if text[i].isdigit():
                if text[i-1].isdigit():
                    return int(text[i-1: i+1])
                return int(text[i])

    return 0


def get_minutes(text):
    global minute_found
    h = 0
    for i in range(len(text)):
        if str(text[i: i+6]) == "minute":
            minute_found = True
            h = i
            break

    i = 0
    if minute_found == True:
        for i in range(h, 0, -1):
            if text[i].isdigit():
                if text[i-1].isdigit():
                    if text[i-2].isdigit():
                        return int(text[i-2: i+1])
                    return int(text[i-1: i+1])
                return int(text[i])

    return 0
