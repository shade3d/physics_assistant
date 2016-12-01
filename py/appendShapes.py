# -----------------------------------------------.
# 物理空間に形状を追加.
#  f_rigidBodyType  ... 剛体の種類.
#  f_softBody       ... ソフトボディ時は1.
#  f_collisionType  ... 衝突形状の種類.
#  f_margin         ... マージン.
#  f_softBodyVolume ... ソフトボディの体積保持時は1.
#  f_softBodyKLST   ... ソフトボディの硬さ.
#  f_softBodyKVC    ... ソフトボディの体積を保つ.
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
except:
    f_rigidBodyType  = 0
    f_collisionType  = 1
    f_softBody       = False
    f_margin         = 0.0
    f_softBodyKLST   = 0.2
    f_softBodyKVC    = 0.0
    f_softBodyVolume = False
    errF = True

scene = xshade.scene()

# --------------------------------------------------.
# ブラウザで選択された形状を0番目の物理シーンに追加.
# --------------------------------------------------.
def appendShapes():
    global result

    # 物理シーンの形状情報を保持.
    phyShapeList = getPhysicsShapesParam()

    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None:
        return

    # 選択形状一覧を取得.
    activeShapesList = []
    for shape in scene.active_shapes:
        # パートの場合はスキップ.
        if shape.type == 2 and shape.part_type == 0:
            continue
        activeShapesList.append(shape)
    
    # 同一形状がすでに物理シーンに存在する場合は更新.
    mass = 1.0
    for shape in activeShapesList:
        index = -1
        for i in range(len(phyShapeList)):
            phyData = phyShapeList[i]
            if phyData[4].ordinal == shape.ordinal:
                index = i
                break
        if index >= 0:
            phyShape = phy.get_shape(index)
            if f_softBody and shape.type != 7:      # ソフトボディ時にポリゴンメッシュでない場合は変更しない.
                continue
            phyData = []
            try:
                phyData.append(f_softBody)
                phyData.append(f_margin)
                phyData.append(mass)
                phyData.append(shape.name)
                phyData.append(shape)
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
                phyShapeList[index] = phyData
            except:
                pass

    # 物理シーンの形状情報を更新.
    updatePhysicsShapes(phyShapeList)

    # 物理シーンに形状追加.
    result = ''
    for shape in scene.active_shapes:
        # パートの場合はスキップ.
        if shape.type == 2 and shape.part_type == 0:
            continue

        phyShape = None
        try:
            if f_softBody == True:
                phyShape = phy.append_softbody_shape(shape, f_softBodyVolume, 0.0, 0.0, f_softBodyKVC, mass, f_margin)
                if phyShape != None:
                    if phyShape.klst >= 0.0:
                        phyShape.klst = f_softBodyKLST
            else:
                phyShape = phy.append_rigidbody_shape(shape, f_collisionType, f_rigidBodyType, mass, f_margin)
            
            # 追加された物理形状のインデックスを取得.
            if phyShape != None:
                index = -1
                for i in range(phy.number_of_shapes):
                    phyShape2 = phy.get_shape(i)
                    if phyShape2.shape.ordinal == phyShape.shape.ordinal:
                        index = i
                        break
                if index >= 0:
                    if result != '':
                        result += ','
                    result += str(index)
            phyShape = None     # 念のための解放処理.
        except:
            pass

    # 物理シーンを更新.
    phy.update()
    return

if errF == False:
   appendShapes()

