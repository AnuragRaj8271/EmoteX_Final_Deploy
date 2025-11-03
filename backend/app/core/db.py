import sqlite3
from pathlib import Path
DB = Path('backend/app/emotex_demo.db')

def get_conn():
    conn = sqlite3.connect(DB)
    return conn
