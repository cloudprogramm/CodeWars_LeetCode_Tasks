import datetime


def unlucky_days(year):
	return len([i for i in range(12) if datetime.date(year, i + 1, 13).weekday() == 4])


print(unlucky_days(2015))
