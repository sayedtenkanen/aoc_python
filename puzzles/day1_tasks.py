from pathlib import Path

from utils.io_lib import read_file_to_string, puzzle_input_file_name, parse_input_string_to_groups

DAY_NUMBER = 1


def task1():
    """
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    """
    print(f"Maximum Calories carried by an Elf is {max(calculate_sums_of_lists())}")


def calculate_sums_of_lists() -> list[int]:
    file_input_string = read_file_to_string(puzzle_input_file_name(day_number=DAY_NUMBER))
    list_of_strings = parse_input_string_to_groups(file_input_string)
    sums_of_lists = []
    for index, value in enumerate(list_of_strings):
        value_list = value.splitlines()
        sums_of_lists.append(sum(list(map(int, value_list))))
    return sums_of_lists


def task2():
    """
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    """
    print(f"Sum of Calories carried by top three Elves is {sum(sorted(calculate_sums_of_lists(), reverse=True)[:3])}")


if __name__ == "__main__":
    task1()
    task2()
