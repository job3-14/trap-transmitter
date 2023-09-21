import board
import busio
import digitalio
import adafruit_ssd1306
import time

# I2C 通信設定
i2c = busio.I2C(board.GP17, board.GP16)  # (SCL端子, SDA端子)

#  液晶画面設定
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C) # 画面サイズ幅,  高さ, 通信仕様, デバイスアドレス


# 引数に表示したいアドレス(0~99)の配列を指定するとOLEDに出力
# 表示可能な配列は最大8個
def showAdress(addressList):
    display.fill(0) # 画面表示初期化
    rect_x = [0, 32, 64, 96, 0, 32, 64, 96]
    rect_y = [0, 0, 0, 0, 29, 29, 29, 29]
    text_x = [3, 35, 67, 99, 3, 35, 67, 99]
    text_y = [7, 7, 7, 7, 36, 36, 36, 36]
    
    for i in range(len(addressList)):
        # 文字表示（"表示内容", x座標, y座標, 色, フォント, サイズ[倍率]）
        display.rect(rect_x[i], rect_y[i], 28, 28, 1)
        number_str = str(addressList[i])
        zero_padded = "0" * (2 - len(number_str)) + number_str
        display.text(zero_padded, text_x[i], text_y[i], 1, font_name="font5x8.bin", size=2)

   
    #display.text('receiving.......', 0, 57, 1, font_name="font5x8.bin", size=1)
    display.show()  # 画面表示実行

def boot():
    display.fill(0) # 画面表示初期化
    display.text('Loading...', 0, 0, 1, font_name="font5x8.bin", size=2)
    display.show()  # 画面表示実行

def receiving():
    display.fill(0) # 画面表示初期化
    display.text('receiving...', 0, 0, 1, font_name="font5x8.bin", size=2)
    display.show()  # 画面表示実行

def error():
    display.fill(0) # 画面表示初期化
    display.text('!!!error!!!', 0, 0, 1, font_name="font5x8.bin", size=2)
    display.text('support\n@alecfoods\n.co.jp', 0, 15, 1, font_name="font5x8.bin", size=2)
    display.hline(0, 15, 128, 1) # (x, y, 長さ, 1)横線
    display.hline(0, 63, 128, 1)        
    display.vline(0, 15, 64, 1) # (x, y, 長さ, 1) 縦線
    display.vline(127, 16, 64, 1)
    display.show()  # 画面表示実行
    while True:
        time.sleep(9999999)