from .connect import connection, TABLE_NAME, SCHEMA
from app.schema.nine_line import NineLineBase

def read_nine_line(id_: str) -> NineLineBase:
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM {TABLE_NAME} where id='{id_}'")
    res = res.fetchone()
    fields = list(SCHEMA.keys())
    values = res if res else [[None] * len(fields)]
    return dict(zip(fields, values))