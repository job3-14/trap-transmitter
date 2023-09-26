from machine import Pin, I2C, UART
import time
import utime

def recive():
    utime.sleep(1)
    for i in range(5):
        buf = uart.read(100)
        utime.sleep(1)
        if buf != None:
            print(buf)
    return

led = machine.Pin(25, machine.Pin.OUT)

# UARTの初期化です。
# UARTの番号とボーレートを指定します。
#uart = UART(0, 9600)
uart = UART(0, 115200)

# init関数はエラーになるので使用できません。
#uart.init(115200,bits=8, parity=None, stop=1 )

#
# データの送信処理です
# 注意：末尾に「\r」をつけないと、データが送信されません。
#
uart.write("mod factory_reset\r")
recive()
#uart.write("lorawan join abp\r")
#recive()
#uart.write("lorawan get_join_status\r")
#recive()
#uart.write("lorawan set_ch_plan AS923\r") #電波法周波数よりAS923以外使用不可
#recive()
#uart.write("lorawan tx ucnf 15 98ba34fd\r") #送信
#recive()
uart.write("p2p set_freq 923200000\r")
recive()
uart.write("p2p set_pwr 20\r")
recive()
uart.write("p2p set_sf 12\r")
recive()
uart.write("p2p set_bw 125\r")
recive()
uart.write("p2p set_cr 4/5\r")
recive()
while True:
    #uart.write("p2p tx 000001\r") #送信
    uart.write("p2p rx 0\r") #受信
    recive()
    utime.sleep(0)
    