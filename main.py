from AutoTypeTool import autoType
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', type=str, help='text to type', required=True)
parser.add_argument('-i', '--interval', type=str, help='interval between each character')
parser.add_argument('-d', '--delay', type=str, help='delay time before auto-type')
args = parser.parse_args()

if __name__ == "__main__":
    interval = 0
    delay = 1
    if args.interval:
        interval = args.interval
    if args.delay:
        delay = args.delay
    autoType(args.text, interval, delay)
