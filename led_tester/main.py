import argparse
import urllib.request

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input

    return filename


def get_input(fname):
    uri = fname
    req = urllib.request.urlopen(uri)
    buffer = req.read().decode('utf-8').split("\n")

    array_size = buffer[0]
    instructions = buffer[1:]

    return array_size, instructions


def generate(array_size):
    myarray = [[True for x in range(array_size)] for y in range(array_size)]
    return myarray



def add(x, y):
    return x + y


if __name__=="__main__":
    # get_input("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    pass