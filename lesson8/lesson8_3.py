from tools import fetch_youbike_data
import streamlit as st
import pandas as pd

youbike_data:list[dict] = fetch_youbike_data()
area_list = list(set(map(lambda value: value['sarea'], youbike_data)))
col1, col2 = st.columns([1,3])
with col1: #col1s內的東西都可以放在這裡
    selected_area = st.selectbox("選擇行政區域", area_list)
    #st.write(selected_area)

with col2:
    def filter_func(value:dict)->bool:
        return value['sarea'] == selected_area
    
    filter_list:list[dict] = list(filter(filter_func, youbike_data))
    show_data:list[dict] = [{
                            '站點':item['sna'],
                            '總車輛數':item['tot'],
                            '可借車輛數':item['sbi'],
                            '可還車輛數':item['bemp'],
                            '營業狀態':item['act'],
                            'latitute':item['lat'],
                            'longitude':item['lng']                                                    
                             } for item in filter_list]
    st.dataframe(show_data)    





#selected_area = col1.selectbox("選擇行政區域", area_list)
#st.write(selected_area)



# youbike_data:list[dict] = fetch_youbike_data()

# # 分2個欄位
# col1, col2 = st.columns(2)

# # 使用youike_data:list的資料，取出所有的行政區域(sarea)，不可以重複
# sareas = list(set([item['sarea'] for item in youbike_data]))

# # 左邊是選擇行政區域(sarea), 使用下拉式表單
# selected_sarea = col1.selectbox('選擇行政區域', sareas)

# # 右邊是顯示該行政區物的YouBike站點資訊的表格資料
# filtered_data = [item for item in youbike_data if item['sarea'] == selected_sarea]
# col2.table(filtered_data)

# # 將資料轉換為DataFrame
# df = pd.DataFrame(filtered_data)

# # 檢查並轉換經緯度資料
# if 'lat' in df.columns and 'lng' in df.columns:
#     # 確保經緯度為數值型態
#     df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
#     df['lng'] = pd.to_numeric(df['lng'], errors='coerce')
#     map_data = df.rename(columns={'lat': 'latitude', 'lng': 'longitude'})
# elif 'latitude' in df.columns and 'longitude' in df.columns:
#     # 確保經緯度為數值型態
#     df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
#     df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
#     map_data = df
# else:
#     st.error('找不到經緯度資料')
#     st.stop()

# # 移除任何包含 NaN 的列
# map_data = map_data.dropna(subset=['latitude', 'longitude'])

# # 顯示地圖
# st.map(map_data)
