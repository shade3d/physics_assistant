# -----------------------------------------------.
# 物理空間内の形状情報を削除.
#  f_selectIndex    ... 選択された形状番号(リストボックスのインデックス)がコンマ区切りで入る.
# -----------------------------------------------.
result = ''

scene = xshade.scene()

errF = False
try:
    selectIndexList = f_selectIndex.split(",")
    f_selectIndex = []
    for i in range(len(selectIndexList)):
        f_selectIndex.append(int(selectIndexList[i]))
    
except:
    f_selectIndex = []
    errF = True

# --------------------------------------------------.
# 0番目の物理シーンから形状を削除.
# --------------------------------------------------.
def removeShapes():
    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None: return

    phyShapesCou = phy.number_of_shapes
    for i in range(phyShapesCou)[::-1]:     # removeでは前詰めされるため、逆から削除していく.
        if i in f_selectIndex:
            phyShape = phy.get_shape(i)
            phyShape.remove()
            phyShape = None     # 念のための解放処理.

    # 物理シーンの更新.
    phy.update()

if errF == False:
    removeShapes()
