import board
import busio
import digitalio
import adafruit_ssd1306

# I2C 通信設定
i2c = busio.I2C(board.GP17, board.GP16)  # (SCL端子, SDA端子)

#  液晶画面設定
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C) # 画面サイズ幅,  高さ, 通信仕様, デバイスアドレス

#  画面表示
display.fill(0) # 画面表示初期化

# 文字表示（"表示内容", x座標, y座標, 色, フォント, サイズ[倍率]）


display.rect(0, 0, 28, 28, 1)
display.rect(32, 0, 28, 28, 1)
display.rect(64, 0, 28, 28, 1)
display.rect(96, 0, 28, 28, 1)
display.rect(0, 29, 28, 28, 1)
display.rect(32, 29, 28, 28, 1)
display.rect(64, 29, 28, 28, 1)
display.rect(96, 29, 28, 28, 1)

display.text("00", 3, 7, 1, font_name="font5x8.bin", size=2)
display.text("01", 35, 7, 1, font_name="font5x8.bin", size=2)
display.text("02", 67, 7, 1, font_name="font5x8.bin", size=2)
display.text("03", 99, 7, 1, font_name="font5x8.bin", size=2)
display.text("04", 3, 36, 1, font_name="font5x8.bin", size=2)
display.text("05", 35, 36, 1, font_name="font5x8.bin", size=2)
display.text("06", 67, 36, 1, font_name="font5x8.bin", size=2)
display.text("07", 99, 36, 1, font_name="font5x8.bin", size=2)

display.text('receiving.......', 0, 57, 1, font_name="font5x8.bin", size=1)
display.show()  # 画面表示実行