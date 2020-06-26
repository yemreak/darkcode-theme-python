import os
import re


def invertHex(hexNumber):
    # invert a hex number
    inverse = hex(abs(int(hexNumber, 16) - 255))[2:]
    # if the number is a single digit add a preceding zero
    if len(inverse) == 1:
        inverse = '0'+inverse
    return inverse


def colorInvert(hexCode):
    # define an empty string for our new colour code
    inverse = ""
    # if the code is RGB
    if len(hexCode) == 6:
        R = hexCode[:2]
        G = hexCode[2:4]
        B = hexCode[4:]
    # if the code is ARGB
    elif len(hexCode) == 8:
        A = hexCode[:2]
        R = hexCode[2:4]
        G = hexCode[4:6]
        B = hexCode[6:]
        # don't invert the alpha channel
        inverse = inverse + A
    else:
        # do nothing if it is neither length
        return hexCode
    inverse = inverse + invertHex(R)
    inverse = inverse + invertHex(G)
    inverse = inverse + invertHex(B)
    return inverse


def replaceHex(matchobj):
    # exclude the preceding hash symbol of the matched object
    hexCode = matchobj.group(0)[1:]
    # invert the colour code and return with the hash
    return '#'+colorInvert(hexCode)


# open and read the original file
""" for path in os.listdir("themes"):
    if "darkcode" in path:
        f = open(f"themes/{path}", 'r').read()

        # invert every match of the regular expression from f
        invertedcode = re.sub('#([0-9a-fA-F]{6})', replaceHex, f)

        g = open(f'themes/{path.replace("darkcode", "lightcode")}', 'w')
        g.write(invertedcode) """


f = open("core/settings.json", "r").read()
invertedcode = re.sub('#([0-9a-fA-F]{6})', replaceHex, f)
g = open("core/inverted-settings.json", 'w')
g.write(invertedcode)
