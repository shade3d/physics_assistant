# -----------------------------------------------.
# Shade3Dの言語チェック.
# -----------------------------------------------.
import os
import time

result = 'en'

win = False
if os.name == "nt" or os.name == "dos":
    win = True
if win:
    if xshade.preference().langid == 1041:
        result = 'ja'
else:
    try:
        result = xshade.preference().locale
    except AttributeError:
        user_text_encoding = os.environ['__CF_USER_TEXT_ENCODING']
        ute = user_text_encoding.split(':')[2]
        if ute == '14':
            result = 'ja'
    except Exception, inst:
        pass
