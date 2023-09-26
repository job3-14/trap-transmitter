import time
import board
import busio

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)

while True:
    uart.write(b'mod factory_reset\r\n')
    print(uart.read())
    uart.write(b'p2p set_freq 923200000\r\n')
    print(uart.read())
    uart.write(b'p2p set_pwr 13\r\n')
    print(uart.read())
    uart.write(b'p2p set_sf 12\r\n')
    print(uart.read())
    uart.write(b'p2p set_bw 125\r\n')
    print(uart.read())
    uart.write(b'p2p set_cr 4/5\r\n')
    print(uart.read())
    time.sleep(10)