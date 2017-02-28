import argparse
import urllib.request
import re
import pprint

class Led:
    def __init__(self, size):
        self.size = size
        self.led_array = self.generate(self.size)


    # This generates the array of leds. True == on, False == off
    def generate(self, array_size):
        myarray = [[True for x in range(array_size)] for y in range(array_size)]
        return myarray

    # switches the leds from x1, y1 to x2, y2 to their opposites
    def switch(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = self.sanitize([x1, y1, x2, y2])

        for i in range(x1, x2):
            for j in range(y1, y2):
                if self.led_array[i][j]:
                    self.led_array[i][j] = False
                else:
                    self.led_array[i][j] = True

    # turns leds on
    def turn_on(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = self.sanitize([x1, y1, x2, y2])

        for i in range(x1, x2):
            for j in range(y1, y2):
                self.led_array[i][j] = True

    # turns leds off
    def turn_off(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = self.sanitize([x1, y1, x2, y2])

        for i in range(x1, x2):
            for j in range(y1, y2):
                self.led_array[i][j] = False

    # turns leds on
    def number_on(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.led_array[i][j]:
                    count += 1
        return count

    # sanitizes input, prevents input from exceeding the boundaries of the led_array
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

    array_size = buffer[0]
    instructions = []

    for i in range(1, len(buffer) - 1):
        reg = re.compile("(turn on|turn off|switch)\s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*through\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)")
        parsed_line = reg.match(buffer[i]).groups()
        if parsed_line:
            instructions.append(parsed_line)

    print(instructions[0][0])

    return array_size, instructions


def main():

    filename = parse_args()
    array_size, instructions = get_input(filename)

    # pprint.pprint(instructions)

    # for elem in instructions:
    #     if elem.startswith("turn on"):
    #         print(elem)
    #
    #     elif elem.startswith("turn off"):
    #         print(elem)
    #
    #     elif elem.startswith("switch"):
    #         print(elem)


if __name__=="__main__":
    main()

    # pprint.pprint(get_input("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"))
