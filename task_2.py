def calculate_difference(sequence: list[int]) -> list[int]:
    diff_list: list[int] = []
    for index, value in enumerate(sequence):
        next_index = index + 1
        if next_index < len(sequence):
            diff_list.append(sequence[next_index] - sequence[index])
    return diff_list


def calculate_all_differences(sequence: list[int]) -> list[list[int]]:
    diff_lists = []

    has_difference = True
    current_sequence = sequence

    while has_difference is True:
        diff_list = calculate_difference(current_sequence)
        if sum(diff_list) == 0:
            has_difference = False

        diff_lists.append(diff_list)
        current_sequence = diff_list
    return diff_lists


def generate_next_diff(sequences: list[list[int]]):
    if len(sequences) == 1:
        return sequences[0][:3]

    non_null_sequences = sequences[:-1]
    for index, diff_list in enumerate(non_null_sequences):
        are_values_equal = all(x == diff_list[0] for x in diff_list)
        step = non_null_sequences[index + 1][0] if len(non_null_sequences) > 1 else 0

        return (
            diff_list[:3]
            if are_values_equal
            else [
                diff_1 := diff_list[-1] + step,
                diff_2 := diff_1 + step,
                diff_2 + step,
            ]
        )


def calculate_next_values(sequence: list[int], diff: list[int]) -> list[int]:
    return [
        number_1 := sequence[-1] + diff[0],
        number_2 := number_1 + diff[1],
        number_2 + diff[2],
    ]


def calculate_next_elements(test_data) -> list[int]:
    sequence = list(map(int, test_data.split()))
    all_differences = calculate_all_differences(sequence)
    diff = generate_next_diff(all_differences)
    return calculate_next_values(sequence, diff)


# Тест 1:
test_data_1 = "12 14 16 18 20"
result_1 = calculate_next_elements(test_data_1)
print("Тест 1:")
print("Вхідні дані:", test_data_1)
print("Вихідні дані:", result_1)

# Тест 2:
test_data_2 = "15 32 57 90 131 180"
result_2 = calculate_next_elements(test_data_2)
print("Тест 2:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)


# Тест 3:
test_data_2 = "1 1 1 1 1"
result_2 = calculate_next_elements(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)

# Тест 4:
test_data_2 = "1 18 43 76 117 166"
result_2 = calculate_next_elements(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)

# # Тест 5:
test_data_2 = "1 2 3 4 5 6"
result_2 = calculate_next_elements(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)

# # Тест 6:
test_data_2 = "11 22 33 44 55"
result_2 = calculate_next_elements(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)
