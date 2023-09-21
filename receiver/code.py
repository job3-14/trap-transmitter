import time
import board
import busio
import binascii
import disp
import config

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)


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

receive_address_list =[]
while True:
    uart.write(b'p2p rx 0\r\n') #受信
    while True:
        rxData = uart.read()
        if rxData is not None:
            break
        time.sleep(1)
    if rxData is not None:
        if 'radio_rx' in rxData:
            rxDataList = rxData.split()
            hexData = rxDataList[2].decode('utf-8')
            byte_data = binascii.unhexlify(hexData)
            hexData = byte_data.decode('utf-8')
            if config.RECEIVE_ADDRESS in hexData:
                index = hexData.find('-')
                number = int(hexData[index+1:])
                if (index != -1) and (number < 100) :
                    receive_address_list.append(number)
                    if len(receive_address_list) > 9:
                        receive_address_list.pop(0)
                    disp.showAdress(receive_address_list)
            print(receive_address_list)
                    
                    
