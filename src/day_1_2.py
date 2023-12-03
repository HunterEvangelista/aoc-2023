import re


def parse_file():
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
        lines = 1
        print(f"on line {lines}")
        for line in input:
            start_point = 0
            current_point = 0
            parsed_line = ""
            while start_point < len(line):
                selection_len = (current_point - start_point) + 1

                if current_point > len(line) - 1:
                    start_point += 1
                    current_point = start_point
                    continue

                # add current element to the parsed string
                if current_point > len(parsed_line) - 1:
                    parsed_line = parsed_line + line[current_point]

                # check conditions to move on to the next start of the search
                if selection_len > 5:
                    start_point += 1
                    current_point = start_point
                    continue
                elif line[current_point].isnumeric():
                    start_point += 1
                    current_point = start_point
                    continue

                # check if current selection spells a number
                current_selection = line[start_point:(current_point + 1)]
                print(f"current_selection: {current_selection}")
                if selection_len < 3:
                    current_point += 1
                    continue
                elif current_selection in number_map.keys():
                    number = number_map[current_selection]
                    diff = len(parsed_line) - current_point
                    parsed_line = parsed_line[:(
                        start_point + 2 + diff)]\
                        + number\
                        + parsed_line[(start_point + 2 + diff):]
                    start_point += 1
                    current_point = start_point
                    continue

                current_point += 1

            lines += 1
            parsed_lines.append(parsed_line)
        return parsed_lines


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
