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
    return MyText
