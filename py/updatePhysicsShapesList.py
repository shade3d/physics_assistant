# -----------------------------------------------.
# 物理形状内で、シーンから削除された形状がある場合に更新.
# return  削除された形状数.
# -----------------------------------------------.
result = ''

scene = xshade.scene()

# 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
phy = getCurrentPhysics()

# シーンから形状が削除された場合は、物理形状を物理シーンから削除する.
def removeNonePhysicsShapes ():
    removeShapeIndex = []
    if phy == None:
        return 0
    shapesCou = phy.number_of_shapes
    for i in range(shapesCou):
        phyShape = phy.get_shape(i)
        if phyShape != None:
            if phyShape.shape == None:
                removeShapeIndex.append(i)
        phyShape = None     # 念のための解放処理.

    if len(removeShapeIndex) > 0:
        for i in range(len(removeShapeIndex))[::-1]:
            phyShape = phy.get_shape(removeShapeIndex[i])
            phyShape.remove()
            phyShape = None     # 念のための解放処理.            
        phy.update()

    return len(removeShapeIndex)

cou = removeNonePhysicsShapes()
if cou > 0:
    result = str(cou)
