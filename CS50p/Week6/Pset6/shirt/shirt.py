import sys
import os
from PIL import Image, ImageOps


def main():
    check_command_line()
    edit_pic()


def edit_pic():
    shirt = Image.open("shirt.png")
    try:
        person = Image.open(sys.argv[1])
        # size
        person = ImageOps.fit(person, shirt.size)

        # merging
        person.paste(shirt, mask=shirt)
        person.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_command_line():
    # command-line len(argv)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # file format
    suffixes = (".jpg", ".jpeg", ".png")

    read_ext = os.path.splitext(sys.argv[1])
    write_ext = os.path.splitext(sys.argv[2])

    if read_ext[1] not in suffixes or write_ext[1] not in suffixes:
        sys.exit("Not a supported file")

    # same file format
    if read_ext[1] != write_ext[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
