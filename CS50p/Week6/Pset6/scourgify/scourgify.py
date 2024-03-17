import sys
import csv


def main():
    check_command_line()
    csv_work()


def csv_work():
    with open(sys.argv[1]) as infile:
        reader = csv.DictReader(infile)

        with open(sys.argv[2], "w") as outfile:
            header = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames = header)
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first, "last": last, "house": house})


def check_command_line():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    read_csv = sys.argv[1]
    write_csv = sys.argv[2]
    if not (read_csv.endswith(".csv") and write_csv.endswith("csv")):
        print("Not a CSV file")
        sys.exit(1)


if __name__ == "__main__":
    main()
