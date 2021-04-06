import re

from utils import colorFormat

MAIN_PATTERN = "(.*?)"


def colored(text, color=None, on_color=None, attr=None):
    """Dyeing the input text.


    The original format is removed from the input text, 
    and the new specified format is applied.

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

    Returns:
        A text of a specific color effect.

    Example:
        colored("Hello, Yang!", "red", "on_grey", "bold")
        colored("Hello, Yang!", "green")
    """

    if color is not None:
        # replace the original color font,example: "\x1b[36mHang\x1b[0m" -> "Hang".
        text = re.sub(colorFormat.COLORS_REGEX + MAIN_PATTERN +
                      colorFormat.RESET_REGEX, r"\1", text)
        text = colorFormat.FMT_STR % (colorFormat.COLORS[color], text)

    if on_color is not None:
        # replace a font with a background color.
        text = re.sub(colorFormat.HIGHLIGHTS_REGEX + MAIN_PATTERN +
                      colorFormat.RESET_REGEX, r"\1", text)
        text = colorFormat.FMT_STR % (colorFormat.HIGHLIGHTS[on_color], text)

    if attr is not None:
        # replace the effect of the original font.
        text = re.sub(colorFormat.ATTRIBUTES_REGEX + MAIN_PATTERN +
                      colorFormat.RESET_REGEX, r"\1", text)
        text = colorFormat.FMT_STR % (colorFormat.ATTRIBUTES[attr], text)

    return text + colorFormat.RESET
