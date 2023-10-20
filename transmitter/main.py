from machine import Pin, I2C, UART
import time
import utime
import config

#LED制御
led = machine.Pin(25, machine.Pin.OUT)
led.value(1)

# UART番号とボーレートを指定
uart = UART(0, 115200)


#通信モジュールからのメッセージを受信(シリアル通信)
def recive():
    utime.sleep(1)
    for i in range(5):
        buf = uart.read(100)
        utime.sleep(1)
        if buf != None:
            #print(buf)  #デバッグ時に使用!!!!!!!!!
            return buf
    return

#LEDを点滅させる
def led_ok():
    for i in range(5):
        led.value(1)
        utime.sleep(0.3)
        led.value(0)
        utime.sleep(0.3)
    return

# 送信設定
def lora_setting():
    uart.write("mod factory_reset\r")
    recive()
    uart.write(f"p2p set_freq {config.frequency[config.channel]}\r") #周波数設定
    recive()
    uart.write(f"p2p set_pwr {config.pwr}\r") # 出力設定
    recive()
    uart.write("p2p set_sf 12\r")
    recive()
    uart.write("p2p set_bw 125\r")
    recive()
    uart.write("p2p set_cr 4/5\r")
    recive()
    uart.write("p2p set_prlen 12\r") #プリアングル長
    recive()
    uart.write("p2p set_crc on\r") #crc
    recive()
    uart.write("p2p set_iqi on\r") #IQ反転
    recive()
    uart.write(f"p2p set_sync {config.SYNC}\r") #同期ワード
    recive()
    return

#送信処理
# checking==1の場合は待機時間を1秒にする
def lora_rx(checking):
    if checking == 1:
        sending_sense = 1
    else:
        sending_sense = config.SENDING_SENSE
    while True:
        uart.write("p2p rx 50\r") #キャリアセンス
        if 'radio_err_timeout' in recive():
            uart.write(f"p2p tx {config.HEX_DATA}\r") #送信
            recive()
            uart.write(f"mod sleep 0 0 {sending_sense}\r") #Loraモジュールの省電力状態にする
            recive()
            break
        else:
            utime.sleep(0.05)
    machine.lightsleep(config.SENDING_SENSE_MS) #RASPIを省電力状態にする
    utime.sleep(0.3) #起動直後は不安定なため待機



def main():
    try:    
        lora_setting()
        lora_rx(1)
    except:
        while True:
            led_ok() #エラー時
    led_ok() #起動完了

    # 送信
    while True:
        try:
            lora_rx(0)
        except:
            lora_setting()

if __name__ == '__main__':
    main()




    

