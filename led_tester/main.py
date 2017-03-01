import numpy as np
import argparse
import urllib.request
import re


class Led:
    def __init__(self, size):
        self.size = size
        self.led_array = np.zeros((self.size, self.size), dtype = bool)


    # turns leds on
    def turn_on(self, x1, y1, x2, y2):
        self.led_array[x1:x2 + 1, y1:y2 + 1] = True


    # turns leds off
    def turn_off(self, x1, y1, x2, y2):
        self.led_array[x1:x2 + 1, y1:y2 + 1] = False


    # switches the leds from x1, y1 to x2, y2 to their opposites
    def switch(self, x1, y1, x2, y2):
        self.led_array[x1:x2 + 1, y1:y2 + 1] ^= True


    # returns number of leds that are on
    def number_on(self):
        return np.sum(self.led_array)


    # prevents input from exceeding the boundaries of the led_array
    def sanitize(self, params):
        for i in range(len(params)):
            if params[i] > self.size:
                params[i] = self.size
            elif params[i] < 0:
                params[i] = 0

        return params


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input

    return filename


def get_input(filename):
    uri = filename
    req = urllib.request.urlopen(uri)
    buffer = req.read().decode('utf-8').split("\n")
    array_size = int(buffer[0])
    instructions = []

    for i in range(1, len(buffer) - 1):
        reg = re.compile("\s*(turn on|turn off|switch)\s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*through\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)")
        parsed_line = reg.match(buffer[i])

        if parsed_line:
            instructions.append(parsed_line.groups())

    return array_size, instructions


def main():

    filename = parse_args()
    array_size, instructions = get_input(filename)

    led = Led(array_size)

    for line in instructions:
        command, x1, y1, x2, y2 = line
        x1, y1, x2, y2 = led.sanitize([int(x1), int(y1), int(x2), int(y2)])

        if command == "turn on":
            led.turn_on(x1, y1, x2, y2)

        elif command == "turn off":
            led.turn_off(x1, y1, x2, y2)

        elif command == "switch":
            led.switch(x1, y1, x2, y2)

    print(led.number_on())

if __name__=="__main__":
    main()

