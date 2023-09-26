from machine import Pin, I2C, UART
import utime

led = machine.Pin(25, machine.Pin.OUT)
# UARTの初期化です。
# UARTの番号とボーレートを指定します。
uart = UART(0, 9600)
#uart = UART(0, 115200)

#
# データの受信処理です
# 1byteずつ読み込んで表示しています。
#
print("read start")

while True:
    buf = uart.read(10)
    text_led_on = 'LED_ON\r'.encode('utf-8')
    text_led_off = 'LED_OFF\r'.encode('utf-8')
    if buf == text_led_on:
        led.value(1)
    if buf == text_led_off:
        led.value(0)
    print(buf)
    utime.sleep(0.1)