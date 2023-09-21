# 設定ファイル(config.py)###############
version = 'v1' #プログラムバージョン
serial = 'FnEC3r9ptE' #シリアルID
SENDING_SENSE = 60
######################################


# HEX_DATA = 製品記号+バージョン+個体識別番号(v1は10桁)
HEX_DATA = f'j314trp+{version}+{serial}'.encode('utf-8').hex()
SENDING_SENSE_MS = SENDING_SENSE * 1000
