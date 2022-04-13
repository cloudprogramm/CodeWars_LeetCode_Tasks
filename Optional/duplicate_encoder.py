# def duplicate_encode(word):
#     return "".join([")" if word.lower().count(i.lower()) > 1 else "(" for i in word])
#
#
# print(duplicate_encode("Success"))


import time


def delay(func):
    def inner(*args, **kwargs):
        if "_seconds" in kwargs:
            second_to_sleep = kwargs.pop("_seconds")
        else:
            second_to_sleep = 3

        print(f"Seconds to sleep: {second_to_sleep}")
        time.sleep(3)
        return func(*args, **kwargs)

    return inner


def seconds_4(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs, _seconds=4)

    return inner


def seconds_5(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs, _seconds=5)
    return inner


@seconds_4
@delay
def double_num(num: int):
    print("Hello, world!")
    return num * 2


double_num(5)
