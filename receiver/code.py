import time
import board
import busio
import binascii
import disp
import config

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)
disp.boot()

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

disp.receiving()
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
            # 文字列に変換
            rxDataList = rxData.split()
            hexData = rxDataList[2].decode('utf-8')
            byte_data = binascii.unhexlify(hexData)
            hexData = byte_data.decode('utf-8')
            # アドレスを画面に表示
            if config.RECEIVE_ADDRESS in hexData: #シリアル番号等が一致しているか確認
                index = hexData.find('-')
                number = int(hexData[index+1:]) #認識番号
                if (index != -1) and (number < 100) and (number not in receive_address_list):
                    receive_address_list.append(number) #受信リストに番号を追加
                    if len(receive_address_list) > 8: # 8個を超えた場合リスト先頭を削除
                        receive_address_list.pop(0)
                    disp.showAdress(receive_address_list) # 画面表示関数を実行