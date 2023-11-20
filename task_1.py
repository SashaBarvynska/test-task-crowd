import re
from typing import Tuple


def transform_text(text: str) -> Tuple[list, list]:
    columns = [int(digit) for x in re.findall(r"\d+", text) for digit in str(x)]
    strings = re.findall(r"[a-zA-Z]+", text)[0]

    text_split_by_groups = []

    index = 0
    while index < len(strings):
        # Split into groups of 2 characters and 1 character
        two_characters = strings[index : index + 2]
        one_characters = strings[index + 2 : index + 3]
        if two_characters:
            text_split_by_groups.append(two_characters)
        if one_characters:
            text_split_by_groups.append(one_characters)
        # Move the index to the next position
        index += 3
    return columns, text_split_by_groups


def generate_encrypt(text: str) -> str:
    # get a list of numbers and list in which text characters are divided into groups of two characters or one character
    columns, text_split_by_groups = transform_text(
        text
    )  # number of columns in the cipher, obtained from the length of columns
    number_of_columns = len(columns)
    # list in which each element is a sublist of characters from text_split_by_groups whose size is number_of_columns
    result = [
        text_split_by_groups[index : index + number_of_columns]
        for index in range(0, len(text_split_by_groups), number_of_columns)
    ]
    string = ""
    column_index_map = {}
    #  keys are numbers from a list of columns, and values ​​are their corresponding indices in that list
    for index, number in enumerate(columns):
        column_index_map[number] = index

    column_index_map = dict(sorted(column_index_map.items()))
    for number in column_index_map.keys():
        for index, value in enumerate(result):
            if len(result) > index + 1:
                string += value[column_index_map[number]]
            else:
                if column_index_map[number] + 1 <= len(value):
                    string += value[column_index_map[number]]
    return string


# Приклад використання:
# Тест 1:
test_data_1 = "41325 INCOMPLETECOLUMNARWITHALTERNATINGSINGLELETTERSANDDIGRAPHS"
result_1 = generate_encrypt(test_data_1)
print("Тест 1:")
print("Вхідні дані:", test_data_1)
print("Вихідні дані:", result_1)

# Тест 2:
test_data_2 = "12 HELLOWORLD"
result_2 = generate_encrypt(test_data_2)
print("Тест 2:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)


# Тест 3:
test_data_2 = "3412 THISISJUSTATEST"
result_2 = generate_encrypt(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)

# Тест 4:
test_data_2 = "165432 WORKSMARTNOTHARD"
result_2 = generate_encrypt(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)

# Тест 5:
test_data_2 = "231 LLOHE"
result_2 = generate_encrypt(test_data_2)
print("Тест 3:")
print("Вхідні дані:", test_data_2)
print("Вихідні дані:", result_2)
