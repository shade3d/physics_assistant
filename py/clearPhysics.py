# -----------------------------------------------.
# カレントの物理シーンをクリアする.
# -----------------------------------------------.
result = ''

# 0番目の物理シーンを取得 (要 : getCurrentPhysics.py).
phy = getCurrentPhysics()

# 物理シーン内の要素をクリア.
if phy != None:
    phy.remove_all_shapes()
    phy.update()

