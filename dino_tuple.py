def create_dino_archive(
        dino_names: list,
        dino_lengths: list,
        dino_diets: list,
) -> list:
    # if all(dino_names) and all(dino_lengths) and all(dino_diets):
    result_tuple = []

    for i in range(len(dino_names)):
        result_tuple.append([])

    # result_tuple = tuple(result_tuple)

    for i in range(len(dino_names)):
        result_tuple[i].append(dino_names[i])
        result_tuple[i].append(dino_lengths[i])
        result_tuple[i].append(dino_diets[i])
        result_tuple[i] = tuple(result_tuple[i])
    print(result_tuple)
    return result_tuple
    # return []


print(create_dino_archive(["Triceratops", "Saltopus"], [9, 1], ["carnivorous", "herbivorous"]))