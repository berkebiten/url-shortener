from pyshorteners import Shortener
from PIL import Image, ImageFont, ImageDraw
from colorama import Fore
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def mapBitToChar(im, col, row):
    if im.getpixel((col, row)):
        return " "
    else:
        return "#"


def output():
    ShowText = " URL Shortener"
    font = ImageFont.truetype("arialbd.ttf", 9)  # load the font
    size = font.getsize(ShowText)  # calc the size of text in pixels
    image = Image.new("1", size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ShowText, font=font)  # render the text to the bitmap
    print(
        Fore.LIGHTCYAN_EX +
        "\n-------------------------------------------------------------------------"
    )
    for r in range(size[1]):
        print(Fore.YELLOW +
              "".join([mapBitToChar(image, c, r) for c in range(size[0])]))
    print(
        Fore.YELLOW +
        "\n                                                        berkebiten (2022)"
    )


def shorten_url(url: str) -> str:
    type_tiny = Shortener()
    short_url = type_tiny.tinyurl.short(url)
    return short_url


def main():
    print(
        Fore.LIGHTCYAN_EX +
        "\n-------------------------------------------------------------------------"
    )
    long_url = input(Fore.LIGHTCYAN_EX + "URL: " + Fore.LIGHTMAGENTA_EX)
    short_url = shorten_url(long_url)
    print(Fore.GREEN + "-> Shortened URL: " + Fore.WHITE + short_url + "\n")


output()
cont = "1"
while cont == "1":
    main()
    cont = input(
        Fore.LIGHTCYAN_EX +
        "Enter \n-> '1' to shorten another URL \n-> '2' to stop the program\n "
        + Fore.LIGHTMAGENTA_EX)
