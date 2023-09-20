# HEX_DATA = 製品記号+バージョン+個体識別番号(v1は10桁)
version = 'v1' #プログラムバージョン
serial = 'FnEC3r9ptE' #シリアルID



HEX_DATA = f'j314trp+{version}+{serial}'.encode('utf-8').hex()
