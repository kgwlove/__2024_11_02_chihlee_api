#module
PI=3.1415926

#建立class
class Person(object):
    '''
    我是Person
    '''
    #init初始化。
    def __init__(self,name:str,age:int): #self可以省略
        self.name = name #attribute
        self.age = age #attribute
        
    #實體方法 instance method。把self傳入echo
    def echo(self):
        print (f'我的名字是:{self.name}')
        print (f'我的年紀是:{self.age}')


#Student class繼承Person
class Student(Person): 
    def __init__(self,name:str,age:int,score:int):
        #初始化副類別Person name-name,第一個是引數名稱,第二個是引數值
        super().__init__(name=name,age=age) 
        self.__score = score #"__" 意思是private

    @property #property一般只能讀。用來防止改score的值
    def score(self)->int: #只能傳出值,不能傳入
        return self.__score

    def echo(self): #overwrite 覆蓋掉上面Person的echo()
        #執行副類別Person的echo
        super().echo()
        print (f'我分數是:{self.score}')



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