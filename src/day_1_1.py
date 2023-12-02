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
