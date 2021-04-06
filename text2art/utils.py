
class colorFormat:
    """Display color format

        `\033[display mode; font color; background color m String\033[0m`

        -------------------------------------------------
        Font color| background color | color description
        -------------------------------------------------
        30        |        40        |       grey
        31        |        41        |       red
        32        |        42        |       green
        33        |        43        |       yellow
        34        |        44        |       blue
        35        |        45        |       magenta
        36        |        46        |       cyan
        37        |        47        |       white
        -------------------------------------------------
        ------------------------------------------------
        display mode   |     effect
        ------------------------------------------------
        0              |     terminal default settings
        1              |     highlight
        4              |     use a underline
        5              |     twinkle
        7              |     anti white display
        8              |     invisible
        ------------------------------------------------
    """

    COLORS = dict(
        list(
            zip([
                "grey",
                "red",
                "green",
                "yellow",
                "blue",
                "magenta",
                "cyan",
                "white"
            ],
                list(range(30, 38))
            )
        )
    )

    HIGHLIGHTS = dict(
        list(
            zip([
                "on_grey",
                "on_red",
                "on_green",
                "on_yellow",
                "on_blue",
                "on_magenta",
                "on_cyan",
                "on_white"
            ],
                list(range(40, 48))
            )
        )
    )

    ATTRIBUTES = dict(
        list(
            zip([
                "bold",
                "dark",
                "underline",
                "blink",
                "reverse",
                "concealed"
            ],
                list(range(1, 9))
            )
        )
    )

    RESET = "\033[0m"
    FMT_STR = "\033[%dm%s"
    RESET_REGEX = "\033\[0m"
    COLORS_REGEX = "\033\[(?:{:s})m".format(
        "|".join([f"{v}" for v in COLORS.values()]))
    HIGHLIGHTS_REGEX = "\033\[(?:{:s})m".format(
        "|".join([f"{v}" for v in HIGHLIGHTS.values()]))
    ATTRIBUTES_REGEX = "\033\[(?:{:s})m".format(
        "|".join([f"{v}" for v in ATTRIBUTES.values()]))
