from datetime import datetime, date
MONTH_DICT = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    expiration_date = expiration_date.split()
    current_date = current_date.split()
    current_date[1] = current_date[1].replace(",", "")
    expiration_date[1] = expiration_date[1].replace(",", "")

    for key, value in MONTH_DICT.items():
        if current_date[0] == key:
            current_date[0] = value

        if expiration_date[0] == key:
            expiration_date[0] = value

    temp_current = date(int(current_date[2]), current_date[0], int(current_date[1]))
    temp_expiration = date(int(expiration_date[2]), expiration_date[0], int(expiration_date[1]))

    print(current_date, expiration_date)

    if temp_current > temp_expiration or entered_code != correct_code:
        return False
    return True


print(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'))
