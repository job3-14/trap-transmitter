# 設定ファイル(config.py)###############
version = 'v1' # プログラムバージョン
serial = 'FnEC3r9ptE' # シリアルID
SENDING_SENSE = 60  # 送信待機時間
number = 0   # 発信番号 0~99
channel = 39 # 周波数チャンネル　！！！ch24-38は簡易無線局要申請！！！
pwr = 13  #20mw->13
sync_10 = 100
######################################


# HEX_DATA = 製品記号+バージョン+個体識別番号(v1は10桁)+登録番号
HEX_DATA = f'j314trp+{version}+{serial}-{number}'.encode('utf-8').hex()
SENDING_SENSE_MS = SENDING_SENSE * 1000
SYNC = hex(sync_10)[2:]

# 周波数リスト(チャンネル:周波数)
# https://www.tele.soumu.go.jp/j/adm/system/ml/920mhz/index.htm (最終確認20231016)
# ch24-38は簡易無線局である為要申請
frequency = {
    # 簡易無線局(要申請)
    24:920600000,
    25:920800000,
    26:921000000,
    27:921200000,
    28:921400000,
    29:921600000,
    30:921800000,
    31:922000000,
    32:922200000,
    33:922400000,
    34:922600000,
    35:922800000,
    36:923000000,
    37:923200000,
    38:923400000,
    # 特定省電力無線曲
    39:923600000,
    40:923800000,
    41:924000000,
    42:924200000,
    43:924400000,
    44:924600000,
    45:924800000,
    46:925000000,
    47:925200000,
    48:925400000,
    49:925600000,
    50:925800000,
    51:926000000,
    52:926200000,
    53:926400000,
    54:926600000,
    55:926800000,
    56:927000000,
    57:927200000,
    58:927400000,
    59:927600000,
    60:927800000,
    61:928000000,
}

