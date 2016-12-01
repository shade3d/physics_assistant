# -----------------------------------------------.
# カレントシーンでの0番目の物理シーン(physics)クラスを取得.
# -----------------------------------------------.

def getCurrentPhysics ():
    scene = xshade.scene()

    # 0番目の物理シーンがなければ作成.
    phyScenesCou = scene.number_of_physics
    if phyScenesCou <= 0:
        scene.create_physics()
    phySceneList = scene.physics_indices    # 物理シーンインデックスの配列を取得.
    if phySceneList == None or len(phySceneList) <= 0:
        return None
    phy = scene.get_physics(phySceneList[0])
    return phy
