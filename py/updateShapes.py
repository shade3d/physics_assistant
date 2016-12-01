# -----------------------------------------------.
# 物理空間内の形状情報を変更.
#  f_rigidBodyType  ... 剛体の種類.
#  f_softBody       ... ソフトボディ時は1.
#  f_collisionType  ... 衝突形状の種類.
#  f_margin         ... マージン.
#  f_softBodyVolume ... ソフトボディの体積保持時は1.
#  f_softBodyKLST   ... ソフトボディの硬さ.
#  f_softBodyKVC    ... ソフトボディの体積を保つ.
#  f_selectIndex    ... 選択された形状番号(リストボックスのインデックス)がコンマ区切りで入る.
#  return 追加された形状番号をコンマ区切りの文字列で返す.
#
#   要 : getCurrentPhysics.py / updateTempShapes.py
# -----------------------------------------------.
result = ''

# 値を数値またはtrue/falseに変換.
errF = False
try:
    f_rigidBodyType = int(f_rigidBodyType)
    f_collisionType = int(f_collisionType)
    f_margin        = float(f_margin)
    f_softBodyKLST  = float(f_softBodyKLST)
    f_softBodyKVC   = float(f_softBodyKVC)
    if f_softBody == '1': f_softBody = True
    else: f_softBody = False
    if f_softBodyVolume == '1': f_softBodyVolume = True
    else: f_softBodyVolume = False

    selectIndexList = f_selectIndex.split(",")
    f_selectIndex = []
    for i in range(len(selectIndexList)):
        f_selectIndex.append(int(selectIndexList[i]))
    
except:
    f_rigidBodyType  = 0
    f_collisionType  = 1
    f_softBody       = False
    f_margin         = 0.0
    f_softBodyKLST   = 0.2
    f_softBodyKVC    = 0.0
    f_softBodyVolume = False
    f_selectIndex    = []
    errF = True

scene = xshade.scene()

# --------------------------------------------------.
# 0番目の物理シーンの情報を更新.
# --------------------------------------------------.
def updateShapes():
    global result

    # 追加/変更する物理形状が 剛体 <==> ソフトボディとなる場合は、.
    # physics.append_softbody_shape/physics.append_rigidbody_shapeではパラメータを変更できない.
    # そのため、一度物理シーン内の形状情報を取得してから物理シーンをクリア、そのあと再追加している.
    
    # 物理シーンの形状情報を保持.
    phyShapeList = getPhysicsShapesParam()
    if phyShapeList == None: return

    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None: return
    
    phyShapesCou = phy.number_of_shapes

    # 作業用のパラメータを更新.
    mass = 1.0
    for i in range(phyShapesCou):
        if i in f_selectIndex:
            if i >= len(phyShapeList): continue
            phyShape = phy.get_shape(i)
            if f_softBody and phyShape.shape.type != 7:      # ソフトボディ時にポリゴンメッシュでない場合は変更しない.
                continue
            phyData = []
            try:
                phyData.append(f_softBody)
                phyData.append(f_margin)
                phyData.append(mass)
                phyData.append(phyShape.name)
                phyData.append(phyShape.shape)
                phyData.append(phyShape.trigger_stop)
                if f_softBody:
                    phyData.append(0.0)
                    phyData.append(0.0)
                    phyData.append(f_softBodyKLST)
                    phyData.append(f_softBodyKVC)
                    phyData.append(f_softBodyVolume)
                else:
                    phyData.append(f_collisionType)
                    phyData.append(f_rigidBodyType)
                phyShapeList[i] = phyData
            except:
                pass

    # 物理シーンの形状情報を更新.
    updatePhysicsShapes(phyShapeList)

    result = ''
    for i in range(phyShapesCou):
        if i in f_selectIndex:
            phyShape = phy.get_shape(i)

            # 追加された物理形状のインデックスをresultに追加.
            if phyShape != None:
                if i >= 0:
                    if result != '':
                        result += ','
                    result += str(i)
                        
            phyShape = None     # 念のための解放処理.                        
    
    # 物理シーンを更新.
    phy.update()
    return
            
if errF == False:
    updateShapes()
