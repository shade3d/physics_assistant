# -----------------------------------------------.
# 0番目の物理シーンから、指定の形状番号に対応するパラメータを取得.
#  f_index 物理形状番号 (0-).
#  return  形状名をコンマで区切ったパラメータの情報を文字列を返す.
#          ==>  形状番号,形状名,マージン,ソフトボディか,   <== 共通.
#               剛体の種類,衝突形状の種類,   <== 剛体情報.
#               ソフトボディの体積を持つ, ソフトボディの硬さ, ソフトボディ形を保つ  <== ソフトボディ情報.
# -----------------------------------------------.
result = ''

errF = False
try:
    f_index = int(f_index)
except:
    errF = True

scene = xshade.scene()

# --------------------------------------------------.
# f_index番目の形状情報を取得.
# --------------------------------------------------.
def getPhysicsShapeParam(index):
    global result

    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None: return
    if index < 0 or index >= phy.number_of_shapes: return

    phyShape = phy.get_shape(index)
    if phyShape == None: return

    try:
        softBodyI = 0
        if phyShape.is_softbody: softBodyI = 1
        result += str(index) + "," + str(phyShape.name) + "," + str(phyShape.margin) + "," + str(softBodyI)
        if phyShape.is_softbody:
            result += ",0,2"    # 静的な剛体(0), ボックス(2).

            softbodyVolumeI = 0
            if phyShape.volume: softbodyVolumeI = 1
            result += "," + str(softbodyVolumeI) + "," + str(phyShape.klst) + "," + str(phyShape.kvc)
        else:
            result += "," + str(phyShape.rigidbody_type) + "," + str(phyShape.collision_type)
            result += ",0,0.2,0.0"  #  ソフトボディの体積を持つ(0), ソフトボディの硬さ(0.2), ソフトボディ形を保つ(0.0).
    except:
        result = ''

    phyShape = None     # 念のための解放処理.

if errF == False:
    getPhysicsShapeParam(f_index)

