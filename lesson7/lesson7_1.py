import requests
from requests import Response
from io import StringIO
from csv import DictReader

url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'


try:
    r:Response = requests.request('GET',url)
    r.raise_for_status()   
except HTTPError as e:
    print(e)
except RequestException as e:
    print(e)
else:
    print("下載成功") #try下方兩行執行都沒有出現錯誤，則執行這一行
    file = StringIO(r.text)
    reader = DictReader(file)
    list_reader:list[dict] = list(reader)
    print(list_reader)