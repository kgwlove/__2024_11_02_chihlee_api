from openpyxl import load_workbook, Workbook, worksheet  #import excel loading tools

def get_aqi(excel_name:str) -> list[dict]:
    wb:Workbook = load_workbook('aqi.xlsx') #load excel file
    sheet:worksheet = wb.worksheets[0]
    type(sheet) #sheet是worksheet , excel中的分頁
    sheets:list = [] #sheets是list
    column_names:list[str] = [cell.value for cell in list(sheet)[0]]
    for row in list(sheet)[1:]:
        site:dict = {column_names[idx]:cell.value for idx,cell in enumerate(row)} #comprehensions寫法
        sheets.append(site) 
    
    return sheets