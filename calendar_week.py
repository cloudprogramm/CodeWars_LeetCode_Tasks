import datetime


def get_calendar_week(date_string):
    result = datetime.datetime.strptime(date_string, "%Y-%m-%d")  # Convert to datetime
    return int(result.strftime('%V'))  # Return weeks to date


print(get_calendar_week("2018-12-31"))  # , 52
