import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        str_list = [str_ for str_ in csv.DictReader(f)]
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(str_list, f, indent=4)


if __name__ == '__main__':
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
