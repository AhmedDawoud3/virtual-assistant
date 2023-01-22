from time import gmtime, strftime
hour_now = int(strftime("%H"))


def welcome_mesage():
    if hour_now >= 6 and hour_now <= 11:
        return "Morning"
    elif hour_now >= 12 and hour_now <= 17:
        return "afternoon"
    elif hour_now >= 18 and hour_now <= 23:
        return "evening"
    else:
        return "night"
