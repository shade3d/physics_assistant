# -----------------------------------------------.
# 物理機能が使用できるかチェック.
# シーンが開いていない場合は0、Physics機能が存在しない場合(Shade3Dのバージョンが古い場合)に-1を返す.
# -----------------------------------------------.
result = '1'

# シーンが存在するかチェック.
try:
    if xshade.scene() == None: result = '0'
except Exception as e:
    result = '0'

# physics機能が使用できるかチェック.
if result == '1':
    try:
        phy = xshade.scene().get_physics(0)
    except Exception as e:
        result = '-1'
