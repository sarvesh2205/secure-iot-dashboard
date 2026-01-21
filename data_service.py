import requests
import pandas as pd
from config import API_URL

def fetch_data():
    r = requests.get(API_URL, timeout=5)
    r.raise_for_status()
    data = r.json()
    return pd.DataFrame(data)
