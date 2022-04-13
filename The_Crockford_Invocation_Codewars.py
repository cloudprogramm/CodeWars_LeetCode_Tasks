def add(a):
    return lambda b: a + b


def subtract(a):
    return lambda b: a - b


def multiply(a):
    return lambda b: a * b


def apply(fn):
    return fn

    # test.assert_equals(add(3)(4), 7);
    # test.assert_equals(subtract(3)(4), -1)
    # test.assert_equals(multiply(3)(4), 12)
    #
    #
    # test.assert_equals(apply(add)(3)(4), 7)
    # test.assert_equals(apply(subtract)(3)(4), -1)
    # test.assert_equals(apply(multiply)(3)(4), 12)
