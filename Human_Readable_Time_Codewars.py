def make_readable(seconds: int) -> str:
    if seconds == 0:
        return "00:00:00"
    if seconds >= 35999:
        return "99:59:59"
    hours = 0
    minutes = 0
    seconds_ = 0

    while seconds > 0:
        if (seconds - 3600) >= 0:
            seconds -= 3600
            hours += 1
        elif (seconds - 60) >= 0:
            seconds -= 60
            minutes += 1
        else:
            seconds_ = seconds
            seconds = 0
    if hours < 10:
        hours = "0" + str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds_ < 10:
        seconds_ = "0" + str(seconds_)
    return f"{hours}:{minutes}:{seconds_}"


print(make_readable(0))
