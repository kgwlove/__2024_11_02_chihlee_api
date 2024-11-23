#練習題11/23老師上課講解
#要求輸入身高,體重
#檢查格式是否錯誤
#計算出BMI,print




#py專案主程式
#使用main()

import tools
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
            Wstate_n,bmi_n= tools.bmiequ(weight,height)

    print(f'您的身高={str(height)}cm,您的體重={weight}kg')            
    print(f'BMI={bmi_n},屬於{Wstate_n}') 



if __name__=='__main__':
    main()
