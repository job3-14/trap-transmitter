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
    uart.write("p2p set_freq 923500000\r")
    recive()
    uart.write("p2p set_pwr 13\r")
    recive()
    uart.write("p2p set_sf 12\r")
    recive()
    uart.write("p2p set_bw 125\r")
    recive()
    uart.write("p2p set_cr 4/5\r")
    recive()
    return

#送信処理
def lora_rx():
    while True:
        uart.write("p2p rx 50\r") #キャリアセンス
        if 'radio_err_timeout' in recive():
            uart.write(f"p2p tx {config.HEX_DATA}\r") #送信
            recive()
            uart.write(f"mod sleep 0 0 {config.SENDING_SENSE}\r") #Loraモジュールの省電力状態にする
            recive()
            break
        else:
            utime.sleep(0.05)
    machine.lightsleep(config.SENDING_SENSE_MS) #RASPIを省電力状態にする
    utime.sleep(0.3) #起動直後は不安定なため待機



def main():
    try:    
        lora_setting()
        lora_rx()
    except:
        while True:
            led_ok() #エラー時
    led_ok() #起動完了

    # 送信
    while True:
        try:
            lora_rx()
        except:
            lora_setting()

if __name__ == '__main__':
    main()




    

