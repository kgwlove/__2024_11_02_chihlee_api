
from pprint import pprint #用來看dictionary資料方便看
import tools

def main():
    data:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')
    sitenames:list=[]
    for item in data:
        sitenames.append(item['sitename'])
    sitenames = list(set(sitenames)) #將sitenames變set,再變成list。沒有重複的項目了
            
    print (len(sitenames))
    pprint (sitenames)

#以下為執行的第一行敘述
if __name__=='__main__':
    main()


        