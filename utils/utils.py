import psycopg2
from psycopg2.extras import NamedTupleCursor
import datetime

def cursor_to_list(cursor):
    results = cursor.fetchall()
    results = [dict(row._asdict()) for row in results]
    return results

def db_connection():
    conn = psycopg2.connect(database="Poc",
                            host="localhost",
                            user="postgres",
                            password="toor")
    cursor = conn.cursor(cursor_factory=NamedTupleCursor)
    return conn,cursor

def data_conversion(data):
    return {
        "fields": {"ID": data["id"],
        "HONORIFIC": "HNR_EN_1",
        "NAME": data['first_name'],
        "LAST_NAME": data['last_name'],
        "BIRTHDATE":datetime.datetime.now(),
        'PHONE': [ { "VALUE": data['phone_number'], "VALUE_TYPE": "WORK" } ] ,
        	"OPENED": "Y","TYPE_ID": "CLIENT",
        }
    }