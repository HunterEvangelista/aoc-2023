import re


def parse_lines_v2():
    number_map = {
        "zero": "ze0ro",
        "one": "o1ne",
        "two": "t2wo",
        "three": "th3ree",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "s6ix",
        "seven": "se7ven",
        "eight": "ei8ght",
        "nine": "ni9ne",
    }
    with open("./data/aoc_2023_day_1_1_input.txt", "r") as input:
        parsed_lines = []
        for line in input:
            parsed_line = line
            for key in number_map.keys():
                parsed_line = re.sub(key, number_map[key], parsed_line)
            parsed_lines.append(parsed_line)

    return parsed_lines


def write_file(parsed_list):
    with open("./data/aoc_2023_day_1_1_parsed.txt", "w") as file:
        file.write("".join(line for line in parsed_list))


def get_numbers():
    ret_list = []
    integers = {str(x) for x in range(0, 10)}
    with open("./data/aoc_2023_day_1_1_parsed.txt") as file:
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
    write_file(parse_lines_v2())
    parsed_lines = get_numbers()
    print(cumulative_sum(parsed_lines))


main()
