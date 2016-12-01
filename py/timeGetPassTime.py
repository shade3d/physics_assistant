# -----------------------------------------------.
# 物理経過時間を取得.
# return  物理シーン内での経過時間.
# -----------------------------------------------.
result = ''

scene = xshade.scene()

# 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
phy = getCurrentPhysics()

if phy != None:
    result = str(phy.pass_time)


