def get_issuer(number):
    str_number = str(number)

    if (str_number.startswith("4") and len(str_number) == 13) or (str_number.startswith("4") and len(str_number) == 16):
        return "VISA"

    card_type = {
        "34": "AMEX",
        "37": "AMEX",
        "6011": "Discover",
        "51": "Mastercard",
        "52": "Mastercard",
        "53": "Mastercard",
        "54": "Mastercard",
        "55": "Mastercard",
    }
    card_lenght = {
        "34": 15,
        "37": 15,
        "6011": 16,
        "51": 16,
        "52": 16,
        "53": 16,
        "54": 16,
        "55": 16,
    }

    for key, value in card_type.items():
        if str_number.startswith(key):
            for key_j, value_j in card_lenght.items():
                if len(str_number) == value_j and str_number.startswith(key):
                    return value
    return "Unknown"



print(get_issuer(4456879456123))