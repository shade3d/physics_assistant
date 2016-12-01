# -----------------------------------------------.
# 物理シーンの形状を実体化する.
# f_partName  パート名.
# -----------------------------------------------.
result = ''

scene = xshade.scene()

# --------------------------------------------------.
# 指定のパート名がルートの何番目に存在するか調べる (最後に見つかったのを返す).
# shapeName  形状名.
# return ルート上の位置(0-).
# --------------------------------------------------.
def findLastShapeIndexByName (shapeName):
    iPos = -1
    findF = False
    try:
        rootShape = scene.shape
        if rootShape.has_son:
            s = rootShape.son
            while s != None:
                iPos += 1
                s = s.bro
                if s.name == shapeName:
                    findF = True
                if s.has_bro == False:
                    break
    except:
        pass

    if findF == False:
        iPos = -1

    return iPos

# --------------------------------------------------.
# 指定のパート名がルートの何番目に存在するか調べる.
# shapeName  形状名.
# return ルート上の位置(0-).
# --------------------------------------------------.
def findShapeIndexByName (shapeName):
    iPos = -1
    fShape = None
    try:
        rootShape = scene.shape
        if rootShape.has_son:
            s = rootShape.son
            while s != None:
                iPos += 1
                s = s.bro
                if s.name == shapeName:
                    fShape = s
                    break
                if s.has_bro == False:
                    break
    except:
        pass

    if fShape == None:
        iPos = -1

    return iPos

# --------------------------------------------------.
# 指定のパート名がルートに存在するか探す.
# shapeName  形状名.
# return 形状の参照.
# --------------------------------------------------.
def findShapeByName (shapeName):
    fShape = None
    try:
        rootShape = scene.shape
        if rootShape.has_son:
            s = rootShape.son
            while s != None:
                s = s.bro
                if s.name == shapeName:
                    fShape = s
                    break
                if s.has_bro == False:
                    break
    except:
        pass

    return fShape

# --------------------------------------------------.
# 0番目の物理シーン内の形状実体化.
# --------------------------------------------------.
def doConvertShape():
    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None: return

    # f_partNameのパート名がルートに存在するか検索.
    fShape = findShapeByName(f_partName)

    if phy.convert_shapes(f_partName, True):
        # 選択状態の追加されたパートにて、表示/非表示フラグの更新.
        scene.show_active()

        # 指定のパート名がルートの何番目に存在するか調べる.
        fShapeIndex = findShapeIndexByName(f_partName)

        # 追加されたパートを、fShapeの1つ前に移動.
        activeShape = scene.active_shape()
        if fShapeIndex >= 0 and fShape != None:
            try:
                # 指定のパート名がルートの何番目に存在するか調べる(最後のものを採用).
                fShapeIndex2 = findLastShapeIndexByName(f_partName)

                if fShapeIndex2 - fShapeIndex >= 1:
                    scene.place_sister(fShapeIndex2 - fShapeIndex)
            except:
                pass
            pass

        if fShape != None:
            fShape.remove()
        
        activeShape.select()

doConvertShape()



