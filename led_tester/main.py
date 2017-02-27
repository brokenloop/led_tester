import argparse
import urllib.request

class Led:
    def __init__(self, size):
        self.size = size
        self.led_array = self.generate(self.size)

    def generate(self, array_size):
        myarray = [[True for x in range(array_size)] for y in range(array_size)]
        return myarray

    def switch(self, x1, y1, x2, y2):
        pass

    def turn_on(self, x1, y1, x2, y2):
        pass

    def turn_off(self, x1, y1, x2, y2):
        pass


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
    instructions = buffer[1:]

    return array_size, instructions


def add(x, y):
    return x + y


if __name__=="__main__":

    led = Led(10)
    print(led.led_array)
    # print(get_input("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"))
