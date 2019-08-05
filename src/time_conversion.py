# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
#       Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.


a = ''


def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == '12':
            a = str('00' + s[2:8])
        else:
            a = s[:-2]
    else:
        if s[:2] == '12':
            a = s[:-2]
        else:
            a = str(int(s[:2]) + 12) + s[2:8]
    return a


s = '11:05:45PM'
result = timeConversion(s)
print(result)
