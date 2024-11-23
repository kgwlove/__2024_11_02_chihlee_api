#練習題11/23老師上課講解
#要求輸入身高,體重
#檢查格式是否錯誤
#計算出BMI,print

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
    
def main():
    try:
        height = float(input('輸入身高cm:'))
    except Exception:
        print('輸入格式錯誤')
    else:
        try:
            weight = float(input('輸入體重kg:'))
        except Exception:
            print('輸入格式錯誤')
        else:
            Wstate_n,bmi_n= bmiequ(weight,height)

    print(f'您的身高={str(height)}cm,您的體重={weight}kg')            
    print(f'BMI={bmi_n},屬於{Wstate_n}') 



if __name__=='__main__':
    main()