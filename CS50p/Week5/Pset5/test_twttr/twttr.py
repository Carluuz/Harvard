import re

def main():
    user = input("Input: ")
    dev = shorten(user)
    print(dev)

def shorten(word):
    dev = re.sub('[AEIOUaeiou]', '', word)
    return dev

if __name__ == "__main__":
    main()



