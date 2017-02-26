from led_tester import main


def first_test():
    assert main.add(2, 2) == 4
    assert main.add(5, 5) == 10
    assert main.add(1, 1) == 3
