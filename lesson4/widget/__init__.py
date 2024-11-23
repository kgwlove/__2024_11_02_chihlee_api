#叫做widget的package:資料夾Widget
PI=3.1415926

class Person:
    pass

def bmiequ(weight, height)->tuple[str,float]:
    '''
    docstring
    parameter:
     bmi:bmi值可以整數或浮點數
    Return:str
         會傳出bmi關聯的體重狀態
    '''
    #BMI僅留小數點兩位
    bmi=round(weight/((height/100)**2), 2)
    if bmi<18.5:
        Wstate='體重過輕'
    elif bmi<24:
        Wstate='正常範圍'
    elif bmi<27:
        Wstate='異常範圍:過重'
    elif bmi<30:
        Wstate='異常範圍:輕度肥胖'
    elif bmi<35:
        Wstate='異常範圍:中度肥胖'      
    else:
        Wstate='異常範圍:重度肥胖'
    return Wstate, bmi