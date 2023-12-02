def parse_file():
    numbers = {
        3: {"one", "two", "six"},
        4: {"four", "five", "nine", "zero"},
        5: {"eight", "three", "seven"},
    }

    number_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    parsed_lines = []
    with open("./data/aoc_2023_day_1_1_input.txt", "r") as input:
        start_point = 0
        current_char = 0
        for line in input:
            parsed_line = ""
            for char in range(line):
                length = (current_char - start_point) + 1
                if line[char].isinteger():
                    # this resets the characters you are looking at
                    start_point += 1
                    current_char = start_point
                elif (length < 3):
                    current_char += 1
                elif length > 5:
                    start_point += 1
                    current_char = start_point

                if length in {*numbers.keys()}:
                    current_chars = line[start_point::current_char + 1]
                    if current_chars in numbers[length]:
                        parsed_line = parsed_line[:start_point] + \
                            number_map[current_chars]
                        current_char += 1
                        start_point = current_char
                        continue

                parsed_line = parsed_line + line[char]
            parsed_lines.append(parsed_line)
    return parsed_lines


def write_file(parsed_list):
    with open("./data/aoc_2023_day_1_1_parsed.txt", "w") as file:
        file.write("\n".join(line for line in parsed_list))


def get_numbers():
    ret_list = []
    integers = {str(x) for x in range(0, 10)}
    with open("./data/aoc_2023_day_1_1_input.txt") as file:
        for line in file:
            first_int = None
            second_int = None
            for char in range(len(line)):
                if line[char] in integers:
                    first_int = char
            for char in range(len(line) - 1, -1, -1):
                if line[char] in integers:
                    second_int = char
            ret_list.append(line[second_int] + line[first_int])
    return ret_list


def cumulative_sum(csv):
    running_sum = 0
    for entry in csv:
        running_sum += int(entry)
    return running_sum


def main():
    parsed_lines = get_numbers()
    print(cumulative_sum(parsed_lines))


main()
