import re

user = input("Input: ")
dev = re.sub('[AEIOUaeiou]', '', user)
print(dev)
