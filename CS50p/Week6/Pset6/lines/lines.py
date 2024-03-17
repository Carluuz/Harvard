import sys

def main():
    comand_line_check()
    file = get_file()
    lines = get_lines(file)
    print(lines)


def get_file():
    argv = sys.argv[1]
    if not argv.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        return open(argv, "r")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(2)


def get_lines(file):
    n_lines = 0
    for line in file:
        line = line.strip()
        if line and not line.startswith("#"):
            n_lines += 1

    file.close()
    return n_lines


def comand_line_check():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)



if __name__ == "__main__":
    main()
