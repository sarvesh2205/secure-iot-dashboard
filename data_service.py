import requests
import pandas as pd
from config import API_URL

def fetch_data():
    try:
        r = requests.get(API_URL, timeout=5)
        r.raise_for_status()
        return pd.DataFrame(r.json())
    except Exception as e:
        # Backend not reachable yet
        return pd.DataFrame()