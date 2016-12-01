# -----------------------------------------------.
# 物理時間を経過させる.
# f_stopTrigger 衝突時に停止させる.
# f_stepTime    経過させる時間  (秒).
# f_mode        物理計算のモード.
#               ''              ... f_stepTime分まとめて計算.
#               'getDivideList' ... f_stepTime分を1/6で分割した際の経過時間リストを取得 ('0.0333,0.0333,001' のように返る).
#               'stepForce'     ... 強制的に f_stepTime時間を進める.
# return   '1' ... 衝突があった場合.
# -----------------------------------------------.
import math
result = ''

scene = xshade.scene()

errF = False
try:
    f_stepTime = float(f_stepTime)

    if f_stopTrigger == '1':
        f_stopTrigger = True
    else:
        f_stopTrigger = False
except:
    f_stepTime = 0.0
    errF = True

try:
    if f_mode == None or f_mode == '':
        f_mode = 'all'      # 経過時間分をまとめて計算.
except:
    pass

minD        = 1.0 / 60.0    # 最小のステップ時間(秒).
subSteps    = int(10)       # ステップ分割数.
isKinematic = True

# --------------------------------------------------.
# 計算の繰り返し回数を取得(途中経過をプログレスバーで出すため).
# --------------------------------------------------.
def getStepLoopCount ():
    if f_stepTime <= minD:
        return 0

    fV = math.fmod(f_stepTime, minD)
    loopCou = int((f_stepTime - fV) * (1.0 / minD))
    return loopCou

# --------------------------------------------------.
# f_stepTimeを、minDで分割したときの計算時間のリストを取得.
# --------------------------------------------------.
def getStepsList ():
    stepsList = []

    # すり抜けを防ぐため、細かく区切る。最小は1/60秒とする.
    fMin        = 0.0000001
    if f_stepTime <= minD:
        stepsList.append(f_stepTime)
    else:
        fV = math.fmod(f_stepTime, minD)
        iCou = getStepLoopCount()
        for i in range(iCou):
            stepsList.append(minD)
        if math.fabs(fV) > fMin:
            stepsList.append(fV)

    return stepsList

# --------------------------------------------------.
# 0番目の物理シーンの時間を経過させる.
# --------------------------------------------------.
def doStep():
    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None: return
    stopF = False

    # 衝突時に計算停止、のフラグを更新.
    shapesCou = phy.number_of_shapes
    for i in range(shapesCou):
        phyShape = phy.get_shape(i)
        if phyShape != None:
            phyShape.trigger_stop = f_stopTrigger      
        phyShape = None     # 念のための解放処理.              

    stepsList = getStepsList()  # 経過時間のリスト.
    for tVal in stepsList:
        phy.step(tVal, subSteps, isKinematic)
        if phy.has_contact == True:       # 衝突がある場合.
            break

# --------------------------------------------------.
# 強制的にf_stepTime時間分進める.
# return  衝突があった場合 '1'が返る.
# --------------------------------------------------.
def doStepForce ():
    fMin = 0.0000001
    if f_stepTime <= fMin:
        return ''
    
    # 0番目の物理シーンを作成 (要 : getCurrentPhysics.py).
    phy = getCurrentPhysics()
    if phy == None: return ''

    # 衝突時に計算停止、のフラグを更新.
    shapesCou = phy.number_of_shapes
    for i in range(shapesCou):
        phyShape = phy.get_shape(i)
        if phyShape != None:
            phyShape.trigger_stop = f_stopTrigger        
        phyShape = None     # 念のための解放処理.

    try:
        phy.step(f_stepTime, subSteps, isKinematic)
    except:
        pass
    if phy.has_contact == True:       # 衝突がある場合.
        return '1'
    return ''

# 経過時間をminDで分割した際の時間リストを取得.
if f_mode == 'getDivideList':
    stepsList = getStepsList()  # 経過時間のリスト.
    result = ''
    for tVal in stepsList:
        if result != None and result != '':
            result += ','
        result += "{0:.7f}".format(tVal)

if errF == False:
    if f_mode == 'all':
        doStep()            # f_stepTime分まとめて計算.

    if f_mode == 'stepForce':
        result = doStepForce()       # 強制的にf_stepTime分計算.


