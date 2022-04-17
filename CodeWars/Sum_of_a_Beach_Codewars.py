import re


def sum_of_a_beach(beach: str) -> int:
    return len(re.findall(r"sand|water|fish|sun", beach, flags=re.IGNORECASE))


print(sum_of_a_beach("SunljjfSuN;sa"))
