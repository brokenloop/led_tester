from led_tester import main
import numpy as np


def test_generate():
    size = 10
    led = main.Led(size)
    assert np.all(led.led_array[0:size + 1, 0:size + 1] == False)


def test_off():
    size = 10
    led = main.Led(size)
    assert np.all(led.led_array[0:size + 1, 0:size + 1] == False)

    led.turn_on(0, 0, size, size)
    led.turn_off(0, 0, size, size)
    assert np.all(led.led_array[0:size + 1, 0:size + 1] == False)

    led.turn_on(0, 0, size, size)
    led.turn_off(0, 0, 4, 4)
    assert led.number_on() == 75


def test_on():
    size = 10
    led = main.Led(size)
    led.turn_on(0, 0, size, size)
    assert np.all(led.led_array[0:size + 1, 0:size + 1])

    led.turn_off(0, 0, size, size)
    led.turn_on(0, 0, 4, 4)
    assert led.number_on() == 25


def test_switch():
    size = 10
    led = main.Led(size)
    led.switch(0, 0, size, size)
    assert np.all(led.led_array[0:size + 1, 0:size + 1])

    led.switch(0, 0, size, size)
    assert np.all(led.led_array[0:size + 1, 0:size + 1] == False)

    led.switch(0, 4, 0, 4)

    assert np.all(led.led_array[0:0, 4:4])


def test_number_on():
    size = 10
    led = main.Led(size)
    led.turn_on(0, 0, size, size)
    assert led.number_on() == size**2

    led.turn_off(0, 0, size, size)
    assert led.number_on() == 0

    led.turn_on(0, 0, 4, 4)
    assert led.number_on() == 25


def test_sanitise():
    size = 10
    led = main.Led(size)
    assert led.sanitize([-10, -5, 0, 5, 10, 15, 20]) == [0, 0, 0, 5, 10, 10, 10]


