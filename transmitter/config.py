# 設定ファイル(config.py)###############
version = 'v1' #プログラムバージョン
serial = 'FnEC3r9ptE' #シリアルID
SENDING_SENSE = 60
number = 0
######################################


# HEX_DATA = 製品記号+バージョン+個体識別番号(v1は10桁)+登録番号
HEX_DATA = f'j314trp+{version}+{serial}-{number}'.encode('utf-8').hex()
SENDING_SENSE_MS = SENDING_SENSE * 1000
