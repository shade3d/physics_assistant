# -----------------------------------------------.
# ウィンドウの各種カラーを取得.
# return  ウィンドウを構成する各種カラー情報をコンマで区切って返す.
#         ウィンドウ背景色,テキスト色,選択時のボタン背景色,枠の色.
#         #c0c0c0,#000000,#f0f040,#000000 のように返す.
# -----------------------------------------------.
result = ''

# ウィンドウ背景色.
backColor = [0.0, 0.0, 0.0]
v = (xshade.preference().base_brightness + 1.0) * 0.44
backColor[0] = v
backColor[1] = v
backColor[2] = v

# テキスト色.
textColor = [0.0, 0.0, 0.0]
if xshade.preference().base_brightness <= 0.2:
    textColor = [1.0, 1.0, 1.0]

# 選択時のボタン色.
buttonBackColor = xshade.preference().selected_control_color

# 枠の色.
boxColor = [0.0, 0.0, 0.0]
v = (0.44 * (xshade.preference().base_brightness + 1.0)) / 0.7
boxColor[0] = v
boxColor[1] = v
boxColor[2] = v

# 色情報を16進数の文字列に.
def convColorToString (val):
    iVal = int(val[0] * 255.0)
    strR = '%02x' % iVal

    iVal = int(val[1] * 255.0)
    strG = '%02x' % iVal

    iVal = int(val[2] * 255.0)
    strB = '%02x' % iVal

    return '#' + strR + strG + strB

backColorStr       = convColorToString(backColor)
textColorStr       = convColorToString(textColor)
buttonBackColorStr = convColorToString(buttonBackColor)
boxColorStr        = convColorToString(boxColor)

result = backColorStr + ',' + textColorStr + ',' + buttonBackColorStr + ',' + boxColorStr
