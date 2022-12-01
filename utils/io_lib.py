"""
Misc IO operations
"""
import os

from puzzle_inputs import PUZZLE_DIR, NEWLINE


def puzzle_input_file_name(day_number: int):
    return os.sep.join([PUZZLE_DIR, f"puzzle_{day_number}.txt"])


def read_file_to_string(file_with_path: str) -> str:
    assert os.path.isfile(file_with_path), f"File {file_with_path} not found"

    with open(file_with_path) as reader:
        return reader.read()


def parse_input_string_to_groups(input_sting: str, splitter: str = NEWLINE):
    return input_sting.split(f"{NEWLINE}{NEWLINE}")


def fibonacci(n):
    temp1, temp2 = 0, 1
    total = 0

    while total < n:
        print(f"total before {total}")
        yield temp1
        print("just entered yield")
        temp3 = temp1 + temp2
        print("temp3 calculated")
        temp1 = temp2
        print("temp1 calculated")
        temp2 = temp3
        print("temp2 calculated")
        total += 1
        print(f"__total after {total}")


if __name__ == "__main__":
    fib_object = fibonacci(20)
    print(list(fib_object))
    value = read_file_to_string(puzzle_input_file_name(1))
    groups = parse_input_string_to_groups(value)
    groups_converted_to_int_lists = {}
    for group in groups:
        print(group.splitlines())