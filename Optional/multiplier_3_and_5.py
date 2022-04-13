# def solution(number):
#     res_list = []
#
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             res_list.append(i)
#     return sum(res_list)
#
#
# print(solution(10))

# *
# def function(first, *args, second, **kwargs):
#     print(first)
#     print(args)
#     print(second)
#     print(kwargs)
#
# function(*[1,2,3], **{ "1": 1}, second=2)


def message_people(people: list):
    names = ""
    for i in people:
        names += i + ", "

    def print_message(message: str):
        if message == "hello":
            print(f"{names} nice to see you!")
        if message == "meeting":
            print(f"{names} we have a meeting in an hour, don't be late!")
        if message == "bye":
            print(f"{names} see you tomorrow!")

    return print_message

mes_people = message_people(["Alex", "Robert", "Tom"])
mes_people('hello')