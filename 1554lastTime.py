def isNotValid(hour, minute):
    if hour < 10:
        hourStr = "0" + str(hour)
    else:
        hourStr = str(hour)

    if minute < 10:
        minuteStr = "0" + str(minute)
    else:
        minuteStr = str(minute)
    mySet = set()
    mySet.add(hourStr[0])
    mySet.add(hourStr[1])
    mySet.add(minuteStr[0])
    mySet.add(minuteStr[1])
    return len(mySet) < 4


def minus1Min(hour, minute):
    minute = minute - 1
    if minute < 0:
        minute = 59
        hour = hour - 1
        if hour < 0:
            hour = 23
    return hour, minute


def lastTime(time):
    if len(time) != 5:
        return "-1"
    split = time.split(':', 1)
    hour = int(split[0])
    minute = int(split[1])

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        return "-1"

    hour, minute = minus1Min(hour, minute)

    while isNotValid(hour, minute):
        hour, minute = minus1Min(hour, minute)

    return str("0" + str(hour) if hour < 10 else hour) + ":" \
           + str("0" + str(minute) if minute < 10 else minute)


print(lastTime("11:22"))
