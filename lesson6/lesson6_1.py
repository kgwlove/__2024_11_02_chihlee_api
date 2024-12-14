import random

def main(): #main主程式 
    set1:set = set() #type hint, set內元素不能重複

    while len(set1) < 7:  #while沒有記憶體區塊
        myrandNum=random.randint(1,49)
        set1.add(myrandNum)
        if len(set1) == 7:
            SpecialNum = myrandNum
            set1.remove(SpecialNum) #移除特別號
            mysetlist = sorted(set1) #6個號碼排序
            break

    mysetlist.append(SpecialNum)
    
    print("本期大樂透電腦選號號碼如下:")
    for num in mysetlist:
        print(num,end=" ")
    print()
    print(f"特別號:{SpecialNum}")        

if __name__ == '__main__':
    main()