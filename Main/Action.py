def straight(robotIP):
    #向前
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    #設定機器人IP


    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

    for i in range(2):
       #TARGET VELOCITY
       X = 0.8 #前後速度，正為前進，負為後退
       Y = 0.0 #橫移速度，正為向左，負為向右
       Theta = 0.0 #旋轉角度，正為順時鐘，負為逆時鐘
       Frequency =0.0 # low speed
       motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)#呼叫走路函數
       time.sleep(1) #暫停1ms

 
    
    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(1)
    #關閉馬達

#向左橫移速度設定
   X = 0.0 
   Y = 0.8
   Theta = 0.0


#向右橫移速度設定
       X = 0.0
       Y = -0.5
       Theta = 0.0

   
#後退速度設定
       X = -0.8 
       Y = 0.0
       Theta = 0.0

#左轉速度設定
       X = 0.1 
       Y = 0.0
       Theta = 0.1

#右轉速度設定
       X = 0.1
       Y = 0.0
       Theta = -0.1


#矩陣傳換成方向

def array_to_dir(A):
    #粗略的循跡
    arr =A[:]
    down=0
    up=0
    c=[0]*5
    print "這是原始C"
    print (c)

    #將機器人的視野拆成上半部與下半部
    for i in range(2,5):
        for j in range(0,5):
            if arr[i][j] ==1:
                down = 1
    #若下半部有黑色格，則設置down為1
    for i in range(0,2):
        for j in range(0,5):
     
            if arr[i][j] ==1:
                up = 1    
    #若上半部有黑色格，則設置up為1
    c=arr[3]            
    print "這是C"
    print (c)
    if (up+down) == 0:#若上下皆為零，表示沒有偵測到黑線
        return 6
    elif down == 0: #若下為零，表示黑線可能有斷點
        return 5
    elif (arr[3][0] >= 1) or (arr[3][1] >= 1):
        #若左邊有黑線，表示機器人偏右，須向左修正
        return 2
    elif (arr[3][4] >= 1) or (arr[3][3] >= 1):
        #若右邊有黑線，表示機器人偏左，須向右修正
        return 3
    else :
        #以上皆非，就是前進的情況
        return 1


#主程式

 s=array_to_dir(A)
        if s ==1:
            print s
            straight(robotIp)
        elif s ==2:
            print s
            leftt(robotIp) #left turn with little degree
        elif s ==3:
            print s
            rightt(robotIp) #right turn with little degree
        elif s ==5:
            print s
            print "前一格無黑線"
            straight(robotIp)

        elif s ==6:
            print s
            print "沒有偵測到黑線"
        t1 = time.time()
        print "移動 delay ", t1 - t0    
