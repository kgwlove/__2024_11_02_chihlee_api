from pprint import pprint #用來看dictionary資料方便看
import openpyxl
from openpyxl import Workbook, worksheet
import tools

def main():
    sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
    wb:Workbook = openpyxl.Workbook()
    sheet:worksheet = wb.active
    sheet.title = "站點名稱"
    for idy ,name in enumerate(sitenames):
        print (name)
        sheet.cell(column=1, row=idy+1, value=name)
    wb.save('老闆要的資訊.xlsx')    

    
#以下為執行的第一行敘述
if __name__=='__main__':
    main()
       