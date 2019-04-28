import records
from sqlalchemy.exc import IntegrityError

db = records.Database('sqllite:///Expenses.sqliteldb.db')

db.query ('''CREATE TABLE IF not EXISTS expenses ())