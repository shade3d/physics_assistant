# -----------------------------------------------.
# 物理シーンの形状を一時保持/まとめて更新する関数.
#   要 : getCurrentPhysics.py
# -----------------------------------------------.

# --------------------------------------------------.
# 物理シーン内の形状情報を一時バッファに保持.
# --------------------------------------------------.
def getPhysicsShapesParam():
    phy = getCurrentPhysics()
    if phy == None: return
    
    phyDataList = []
    phyShapesCou = phy.number_of_shapes
    for i in range(phyShapesCou):
        phyShape = phy.get_shape(i)
        phyData = []
        try:
            phyData.append(phyShape.is_softbody)
            phyData.append(phyShape.margin)
            phyData.append(phyShape.mass)
            phyData.append(phyShape.name)
            phyData.append(phyShape.shape)
            phyData.append(phyShape.trigger_stop)
            if phyShape.is_softbody:
                phyData.append(phyShape.kdf)
                phyData.append(phyShape.kdp)
                phyData.append(phyShape.klst)
                phyData.append(phyShape.kvc)
                phyData.append(phyShape.volume)
            else:
                phyData.append(phyShape.collision_type)
                phyData.append(phyShape.rigidbody_type)
        except:
            pass
        phyDataList.append(phyData)
        phyShape = None
    return phyDataList

# --------------------------------------------------.
# 物理シーンを一度クリアしてからすべて更新.
# --------------------------------------------------.
def updatePhysicsShapes(phyDataList):
    phy = getCurrentPhysics()
    if phy == None: return

    phy.remove_all_shapes()

    sCou = len(phyDataList)
    for i in range(sCou):
        phyData = phyDataList[i]
        if len(phyData) <= 6: continue

        is_softbody  = phyData[0]
        margin       = phyData[1]
        mass         = phyData[2]
        name         = phyData[3]
        shape        = phyData[4]
        trigger_stop = phyData[5]
        if is_softbody:
            kdf    = phyData[6]
            kdp    = phyData[7]
            klst   = phyData[8]
            kvc    = phyData[9]
            volume = phyData[10]
            phyShape = phy.append_softbody_shape(shape, volume, kdf, kdp, kvc, mass, margin)
            if phyShape != None:
                phyShape.klst = klst
        else:
            collison_type  = phyData[6]
            rigidbody_type = phyData[7]
            phyShape = phy.append_rigidbody_shape(shape, collison_type, rigidbody_type, mass, margin)
        phyShape = None

