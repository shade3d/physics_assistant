# -----------------------------------------------.
# 0番目の物理シーンから、形状名一覧を取得 (リストボックスに表示するため).
#  return  形状名をコンマで区切った文字列を返す.
# -----------------------------------------------.
result = ''

scene = xshade.scene()

# 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
phy = getCurrentPhysics()

if phy != None:
    shapesCou = phy.number_of_shapes
    for i in range(shapesCou):
        if i > 0:
            result += ','
        phyShape = phy.get_shape(i)
        try:
            if phyShape != None and phyShape.shape != None:
                result += str(phyShape.shape.name)
        except:
            pass
        phyShape = None     # 念のための解放処理.
