# text2art [![Version][version-badge]][version-link] ![MIT License][license-badge]

`text2art` is Python implementation of the original Figlet project. It looks like this (although you can select your font and color):

```
      .-') _     ('-.  ) (`-.      .-') _               ('-.     _  .-')   .-') _
     (  OO) )  _(  OO)  ( OO ).   (  OO) )             ( OO ).-.( \( -O ) (  OO) )
     /     '._(,------.(_/.  \_)-./     '._  .-----.   / . --. / ,------. /     '._
     |'--...__)|  .---' \  `.'  / |'--...__)/ ,-.   \  | \-.  \  |   /`. '|'--...__)
     '--.  .--'|  |      \     /\ '--.  .--''-'  |  |.-'-'  |  | |  /  | |'--.  .--'
        |  |  (|  '--.    \   \ |    |  |      .'  /  \| |_.'  | |  |_.' |   |  |
        |  |   |  .--'   .'    \_)   |  |    .'  /__   |  .-.  | |  .  '.'   |  |
        |  |   |  `---. /  .'.  \    |  |   |       |  |  | |  | |  |\  \    |  |
        `--'   `------''--'   '--'   `--'   `-------'  `--' `--' `--' '--'   `--'
                                                                --------- by HangfengYang
```


### Getting Started
---

#### help
```
>>> text2art h
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
```

#### Generates random fonts and random colors.

```
>>> text2art rd yang

                                                       /
                      Y88b  /   /~~~8e  888-~88e e88~88e
                       Y888/        88b 888  888 888 888
                        Y8/    e88~-888 888  888 "88_88"
                         Y    C888  888 888  888  /
                        /      "88_-888 888  888 Cb
                      _/                          Y8""8D
```

#### Random display of 25 fonts

```
>>> text2art lf
```

#### Generate ascii art text via given font

```
>>> text2art gt yang --font ghost

                               ('-.         .-') _
                              ( OO ).-.    ( OO ) )
                   ,--.   ,--./ . --. /,--./ ,--,'  ,----.
                    \  `.'  / | \-.  \ |   \ |  |\ '  .-./-')
                  .-')     /.-'-'  |  ||    \|  | )|  |_( O- )
                 (OO  \   /  \| |_.'  ||  .     |/ |  | .--, \
                  |   /  /\_  |  .-.  ||  |\    | (|  | '. (_/
                  `-./  /.__) |  | |  ||  | \   |  |  '--'  |
                    `--'      `--' `--'`--'  `--'   `------'
```

#### Generate ascii art text via given color

```
>>> text2art gt hang --color cyan
>>> text2art gt hang --color red
```

![COLOR][colored]



#### Adjust the properties of the font

```
>>> text2art gt hang 
>>> text2art gt hang --attr bold
```
![ATTR][attr]

#### Adjust the background color

```
>>> text2art gt hang --on_color on_cyan --color yellow --attr bold
```

![ON_COLOR][on_color]


#### Adjust the location of the output font

```
>>> text2art gt feng --color cyan # default center
>>> text2art gt feng --color cyan --justify left
```

![JUSTIFY][justify]

#### Adjust the width of the terminal background

```
>>> text2art gt suibianshu # default width is 80
>>> text2art gt suibianshu --width 120
```

![WIDTH][width]

### Installation
---

`text2art` is hosted on [PYPI](https://pypi.python.org/pypi/text2art) and can be installed as such:

```
>>> pip install text2art
```

Alternatively, you can also get the latest source code from [GitHub](https://github.com/Fenghuapiao/text2art) and install it manually:

```
>>> git clone git@github.com:Fenghuapiao/text2art.git
>>> cd text2art
>>> python setup.py install
```

For update:

```
>>> pip install text2art --upgrade
```

### Questions

* The color display in DOS uses the init method in the colorama package. How can it be implemented without calling additional packages?

* How fire packages are friendly output help documents?

### Last

very welcome to star and pull requests, and I hope you can submit a nice font or color scheme to Issue.

### License
---

MIT ([here](https://github.com/Fenghuapiao/text2art/blob/master/LICENSE))


[version-badge]: https://img.shields.io/pypi/v/text2art.svg?label=version
[version-link]: https://pypi.python.org/pypi/text2art/
[license-badge]: https://img.shields.io/badge/license-MIT-007EC7.svg

[colored]: https://raw.githubusercontent.com/Fenghuapiao/text2art/master/screenshot/colored.png
[justify]: https://raw.githubusercontent.com/Fenghuapiao/text2art/master/screenshot/justify_left.png
[on_color]: https://raw.githubusercontent.com/Fenghuapiao/text2art/master/screenshot/on_color.png
[attr]: https://raw.githubusercontent.com/Fenghuapiao/text2art/master/screenshot/set_attr.png
[width]: https://raw.githubusercontent.com/Fenghuapiao/text2art/master/screenshot/set_width.png