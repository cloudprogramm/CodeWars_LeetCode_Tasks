from typing import List


def pendulum(values: List[int]) -> List[int]:
    pendulum_values = list()
    sorted_values = sorted(values)

    for iter_, value in enumerate(sorted_values):
        if iter_ % 2 != 0:
            pendulum_values.append(value)
        else:
            pendulum_values.insert(0, value)
    return pendulum_values

    # pendulum_values = list()
    # iter_ = 1
    #
    # while len(values) != 0:
    #     min_value = min(values)
    #     if iter_ % 2 == 0:
    #         pendulum_values.append(min_value)
    #     else:
    #         pendulum_values.insert(0, min_value)
    #
    #     iter_ += 1
    #     index_ = values.index(min_value)
    #     values.pop(index_)
    #
    # return pendulum_values


print(pendulum([4, 6, 8, 7, 5]))  # , [8,6,4,5,7])
