#!/usr/bin/python3
"""class cstr that inherists from str"""


colors = {
    'black': '\u001b[30m', 'red': '\u001b[31m', 'green': '\u001b[32m',
    'yellow': '\u001b[33m', 'blue': '\u001b[34m', 'magenta': '\u001b[35m',
    'cyan': '\u001b[36m', 'white': '\u001b[37m',
    'reset': '\u001b[0m'
}


class cstr(str):
    """A class derived from str that allows to print colored strings easily.
    The following methods will always return a str instance you can use for
    any purpose"""


    def __init__(self, string):
        """stores its original string as a property"""
        self.string = string


    def color(self, value=None):
        """returns a colored string, works with str ('black', 'red', 'green',
        'yellow', 'blue', 'magenta', 'cyan', 'white', 'reset') and int
        (from 0 to 255)"""
        if not value:
            return self
        else:
            if type(value) is int and 0 <= value <= 255:
                return "\u001b[38;5;{}m{}{}".format(value, self.string,
                                                    colors['reset'])
            elif value not in colors:
                raise ValueError("Not a valid color")
            else:
                cl = colors[value]
                return "{}{}{}".format(cl, self.string, colors['reset'])


    def bright(self, value=None):
        """returns a bright colored string, only works with str"""
        if not value:
            return self
        else:
            if value not in colors:
                raise ValueError("Not a valid color")
            else:
                cl = colors[value]
                return "{}{}{}".format(cl.replace('m', ';1m'), self.string,
                               colors['reset'])


    @property
    def uncolored(self):
        """if you have a colored string with raw format, you can extract the
        string without its encoded colors with this method"""
        import re

        string = self.string
        encodedColors = re.findall("\\u001b\[[^m]{1,8}m{1}", string)
        for color in encodedColors:
            string = string.replace(color, '')
        return string
