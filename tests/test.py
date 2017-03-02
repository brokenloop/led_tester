from led_tester import main


def test_generate():
    size = 10
    myarray = main.Led(size)

    for i in range(size):
        for j in range(size):
            assert myarray.led_array[i][j] == False


def test_off():
    size = 10
    led = main.Led(size)
    led.turn_off(0, 0, size, size)
    for i in range(size):
        for j in range(size):
            assert led.led_array[i][j] == False

    led.turn_on(0, 0, size, size)
    led.turn_off(size, size, 0, 0)
    for i in range(size):
        for j in range(size):
            assert led.led_array[i][j] == False




def test_on():
    size = 10
    led = main.Led(size)
    led.turn_off(0, 0, size, size)
    led.turn_on(0, 0, size, size)
    for i in range(size):
        for j in range(size):
            assert led.led_array[i][j] == True

    led.turn_off(0, 0, size, size)
    led.turn_on(size, size, 0, 0)
    for i in range(size):
        for j in range(size):
            assert led.led_array[i][j] == True


def test_switch():
    size = 10
    led = main.Led(size)
    led.switch(0, 0, size, size)
    for i in range(size):
        for j in range(size):
            assert led.led_array[i][j] == False

    led.switch(0, 0, size, size)
    for i in range(size):
        for j in range(size):
            assert led.led_array[i][j] == True


def test_number_on():
    size = 10
    led = main.Led(size)
    assert led.number_on() == size**2

    led.turn_off(0, 0, size, size)
    assert led.number_on() == 0


def test_sanitise():
    size = 10
    led = main.Led(size)
    assert led.sanitize([-5, 0, 5, 10, 15]) == [0, 0, 5, 10, 10]


