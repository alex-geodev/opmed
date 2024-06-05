# https://docs.python.org/3/library/sqlite3.html

import sqlite3

connection = sqlite3.connect("ninelines.db")
TABLE_NAME = "ninelines"
SCHEMA = {
    "id": "integer primary key",
       "audio_transcription": "text",
        "audio_file": "text",
        "mgrs": "text",
        "lat" :"real",
        "lon": "real",
        "frequency": "text",
        "urgent": "integer",
        "urgent_surgical": "integer",
        "priority": "integer",
        "routine": "integer",
        "convenience": "integer",
        "litter": "integer",
        "ambulatory": "integer",
        "us_military": "integer",
        "us_civilian": "integer",
        "non_us_military": "integer",
        "non_us_civilian": "integer",
        "enemy_prisoner_of_war": "integer",
        "equipment": "text",
        "site_security": "text",
        "pickup_mark": "text",
        "cbrn": "text"
}

def create_table():
    cursor = connection.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({', '.join(k + ' ' + v for k, v in SCHEMA.items())})"
    cursor.execute(query)

def insert(
    id_,
    audio_transcription,
    audio_file,
    mgrs,
    lat,
    lon,
    frequency,
    urgent,
    urgent_surgical,
    priority,
    routine,
    convenience,
    litter,
    ambulatory,
    us_military,
    us_civilian,
    non_us_military,
    non_us_civilian,
    enemy_prisoner_of_war,
    equipment,
    site_security,
    pickup_mark,
    cbrn
):
    create_table()

    cursor = connection.cursor()
    query = f"insert into {TABLE_NAME} values ({id_}, '{mgrs}',\
        '{audio_transcription}', '{audio_file}', '{lat}', '{lon}', \
        '{frequency}', '{urgent}', '{urgent_surgical}', '{priority}',\
        '{routine}', '{convenience}', '{litter}', '{ambulatory}',\
        '{us_military}', '{us_civilian}', '{non_us_civilian}',\
        '{enemy_prisoner_of_war}', '{equipment}', '{site_security}', '{pickup_mark}', '{cbrn}')"
    
    cursor.execute(query)
    connection.commit()

def fetch_one_by_id(id_):
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM {TABLE_NAME} where id='{id_}'")
    res = res.fetchone()
    fields = list(SCHEMA.keys())
    values = res if res else [[None] * len(fields)]
    return dict(zip(fields, values))
