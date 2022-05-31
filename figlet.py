"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
import random
import argparse
from pyfiglet import Figlet

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='FIGlet - ASCII art',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    #parser.add_argument('text',
    #                    metavar='text',
    #                    type=str,
    #                    help='Input string or file')

    parser.add_argument('-f',
                        '--font',
                        help='fontname',
                        metavar='str',
                        type=str)
                      
    args = parser.parse_args()

    #if os.path.isfile(args.text):
    #    args.text = open(args.text).read().rstrip()

    return args

def main():
    figlet = Figlet()
    font_list = figlet.getFonts()
    args = get_args()

    if len(sys.argv) == 1:
        f = random.choice(font_list)
    else:
        f = args.font
        if f not in font_list:
            sys.exit('Invalid usage')

    
    txt = input("Input: ")



    figlet.setFont(font=f)
    print(figlet.renderText(txt))

if __name__ == '__main__':
    main()
