import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    src = re.search(r'src="https?://(?:www.)?youtube.com/embed/([^"]+)"', s)
    if src:
        vid_id = src.group(1)
        prefix = "https://youtu.be/"
        return prefix + vid_id
    return None

if __name__ == "__main__":
    main()
