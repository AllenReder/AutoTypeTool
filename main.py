from AutoTypeTool import autoType
from window import getArgsFromWindow
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', type=str, help='text to type')
parser.add_argument('-i', '--interval', type=str,
                    help='interval between each character')
parser.add_argument('-d', '--delay', type=str,
                    help='delay time before auto-type')
args = parser.parse_args()

interval = 0.01
delay = 1

if __name__ == "__main__":
    if not args.text:   # Window version
        text, interval, delay = getArgsFromWindow()
    else:   # Command Args version
        text = args.text
        if args.interval:
            interval = args.interval
        if args.delay:
            delay = args.delay
    autoType(text, interval, delay)
