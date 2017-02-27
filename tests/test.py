from led_tester import main


def first_test():
    assert main.add(2, 2) == 4
    assert main.add(5, 5) == 10
    assert main.add(1, 1) == 2


def test_generate():
    size = 10
    myarray = main.Led(size)
    assert len(myarray.led_array) == size

    for i in range(size):
        assert len(myarray.led_array[i]) == size
        for j in range(size):
            assert myarray.led_array[i][j] == True


def test_commands():
    
    size = 10
    x1, y1, x2, y2 = 0, 0, 5, 5
    led = main.Led(size)
    led.turn_off(x1, y1, x2, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            assert led.led_array[i][j] == False

    led.turn_on(x1, y1, x2, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            assert led.led_array[i][j] == True

    led.switch(x1, y1, x2, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            assert led.led_array[i][j] == False

