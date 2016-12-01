# -----------------------------------------------.
# 物理時間をリセットする.
# -----------------------------------------------.
result = ''

scene = xshade.scene()

# 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
phy = getCurrentPhysics()

if phy != None:
    phy.reset_step()

