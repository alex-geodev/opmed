from .connect import connection, TABLE_NAME, SCHEMA, neo4j_connection
from app.schema.nine_line import NineLineBase
from app.schema.coas import COABase
from typing import List

def get_nine_lines() -> List[NineLineBase]:
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    res = res.fetchall()
    fields = list(SCHEMA.keys())
    resp = []
    if len(res) > 0:
        for calls in res:
            resp.append(dict(zip(fields, calls)))
    return resp

def get_nine_line(id_: str) -> NineLineBase:
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM {TABLE_NAME} where id='{id_}'")
    res = res.fetchone()
    fields = list(SCHEMA.keys())
    values = res if res else [[None] * len(fields)]
    return dict(zip(fields, values))

def get_coas() -> List[COABase]:
    print(neo4j_connection)
    # TODO: put in the methods here to connect to the neo4j and pull back as a list of COA objects.
    return[{'id': "example"}]