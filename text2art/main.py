import random
from pyfiglet import Figlet, FigletFont

import fire
from colorama import init

from color import colored
from utils import colorFormat

DEFAULT_FONT = "ghost"
font_list = FigletFont.getFonts()
# Key value pair reversal
color_dict = {value: key for key, value in colorFormat.COLORS.items()}


def lf():
    """Random display of 25 fonts"""
    return random.sample(font_list, 25)


def rd(text, on_color=None, attr=None,
       width=80, justify="center"):
    """An art font that generates random fonts 
       and random colors.


       Args:
        text: Get an character string.
        color: Get a color string,dye the input string 
               with the corresponding color.
        available text colors:
               red, green, yellow, blue, magenta, cyan, white.
        on_color: Get an character string,setting the background 
                  color of the text.
        available text highlights:
            on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, 
            on_white.
        attr: Get a character string,setting the effect of the text.
        available attributes:
                bold, dark, underline, blink, reverse, concealed.

        width: Setting the terminal width of the output font, type is int.
        justify: Setting the location of the terminal output font.
        available parameter: left, enter, right.

    Returns:
        A text of a specific color effect.
    """
    rand_int = random.randint(1, len(font_list)+1)
    rand_color = color_dict.get(random.randint(30, 38))

    rand_font = font_list[rand_int]
    print(f"Random font: {format(rand_font)}")
    f = Figlet(
        font=rand_font, width=width,
        justify=justify
    )
    r = f.renderText(text)
    return colored(r, rand_color, on_color, attr)


def gt(text, font=DEFAULT_FONT, color="magenta",
       on_color=None, attr=None, width=80,
       justify="center"):
    """An art font that generates the effect of 
       the specified parameter.


       Args:
        text: Get an character string.
        on_color: Get an character string,setting the background 
                  color of the text.
        available text highlights:
            on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, 
            on_white.
        attr: Get a character string,setting the effect of the text.
        available attributes:
                bold, dark, underline, blink, reverse, concealed.

        width: Setting the size of the terminal output font, type is int.
        justify: Setting the location of the terminal output font.
        available parameter: left, enter, right.

    Returns:
        A text of a specific color effect.

    """

    f = Figlet(
        font, width=width,
        justify=justify
    )
    r = f.renderText(text)
    return colored(r, color, on_color, attr)


def h():
    doc = """
            Usage:
                text2art lf  # Random display of 25 fonts
                text2art rd text [--on_color] [--attr] [--width] [--justify]
                text2art gt text [--font] [--color] [--on_color] [--attr] [--width] [--justify]

            available text colors:
                red, green, yellow, blue, magenta, cyan, white.

            available text highlights:
                on_red, on_green, on_yellow, on_blue, on_magenta, 
                on_cyan,on_white.

            available attributes:
                bold, dark, underline, blink, reverse, concealed.

            width: Setting the size of the terminal output font,type is int.
            justify: Setting the location of the terminal output font.
            available parameter: left, enter, right.
          """
    print(doc)


def main():
    init(autoreset=True)
    fire.Fire()


if __name__ == '__main__':
    main()
