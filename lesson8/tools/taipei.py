from typing import List, Dict, Optional
import requests
from requests import Response
from io import StringIO
from csv import DictReader
from requests.exceptions import RequestException, HTTPError
import streamlit as st
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@st.cache_data
def get_youbikes() -> List[Dict[str, str]]:
    """
    從新北市政府開放資料平台獲取YouBike站點資訊
    
    Returns:
        List[Dict[str, str]]: YouBike站點資訊列表
    
    Raises:
        Exception: 當發生HTTP錯誤或連線問題時
    """
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'
    
    try:
        response: Response = requests.get(url, timeout=10)
        response.raise_for_status()
        
    except HTTPError as http_err:
        logger.error(f"HTTP錯誤: {http_err}")
        raise Exception("伺服器連線錯誤，請稍後再試") from http_err
        
    except RequestException as req_err:
        logger.error(f"請求錯誤: {req_err}")
        raise Exception("網路連線問題，請檢查網路設定") from req_err
        
    try:
        file = StringIO(response.text)
        reader = DictReader(file)
        bikes_data: List[Dict[str, str]] = list(reader)
        
        if not bikes_data:
            raise ValueError("未獲取到YouBike資料")
            
        logger.info(f"成功獲取 {len(bikes_data)} 筆YouBike資料")
        return bikes_data
        
    except (ValueError, Exception) as e:
        logger.error(f"資料處理錯誤: {e}")
        raise Exception("資料處理發生錯誤") from e