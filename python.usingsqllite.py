import requests
import records
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlalchemy.exc import IntegrityError

db = records.Database('sqllite:///crawler_database.db')
db.query('''CREATE TABLE IF NOT EXISTS links (
    url text primary key,
    created_at datetime,
    visited_at datetime NULL)''')

db.query(''' CREATE TABLE IF NOT EXISTS numbers (url tet, number integer)''')
