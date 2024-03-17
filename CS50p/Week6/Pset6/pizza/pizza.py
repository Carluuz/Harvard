import sys
import csv
from tabulate import tabulate


def main():
    comand_line_check()
    table = get_csv()
    print_tabulate(table)


def get_csv():
    argv = sys.argv[1]
    if not argv.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        table = []

        with open(argv) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append({"pizza": row[0], "small": row[1], "large": row[2]})
            return table
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(2)


def print_tabulate(table):
    print(tabulate(table[1:], table[0], tablefmt="grid"))


def comand_line_check():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)


if __name__ == "__main__":
    main()
