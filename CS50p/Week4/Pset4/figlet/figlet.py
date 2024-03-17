import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            figlet.setFont(font = sys.argv[2])
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
elif len(sys.argv) == 1:
    figlet(font = random.choice(fonts))
else:
    print("Invalid usage")
    sys.exit(1)


text = input("Input: ")
print(figlet.renderText(text))

# made in CS50x week6 
