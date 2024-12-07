
from pprint import pprint #用來看dictionary資料方便看
import tools

def main():
    sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
    print (len(sitenames))
    pprint (sitenames)
    
#以下為執行的第一行敘述
if __name__=='__main__':
    main()


        