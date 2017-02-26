from led_tester import main


def first_test():
    assert main.add(2, 2) == 4
    assert main.add(5, 5) == 10
    assert main.add(1, 1) == 2


def generate_test():
    size = 10
    myarray = main.generate(size)
    assert len(myarray) == size

    for i in range(size):
        assert len(myarray[i]) == size
        for j in range(size):
            assert myarray[i][j] == True

generate_test()
