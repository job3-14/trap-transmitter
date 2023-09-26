from machine import Pin, I2C, UART
import time
import utime

led = machine.Pin(25, machine.Pin.OUT)

# UARTの初期化です。
# UARTの番号とボーレートを指定します。
uart = UART(0, 9600)
#uart = UART(0, 115200)

# init関数はエラーになるので使用できません。
#uart.init(115200,bits=8, parity=None, stop=1 )

#
# データの送信処理です
# 注意：末尾に「\r」をつけないと、データが送信されません。
#
while True:
    uart.write("LED_ON\r")
    led.value(1)
    utime.sleep(1)
    uart.write("LED_OFF\r")
    led.value(0)
    utime.sleep(1)
    
