from sqlalchemy import Table, Column, Integer, String, MetaData, Text, Float, insert
from sqlalchemy import create_engine
from data_manager.data_manager import data_manager1, data_manager2

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

clean_measure = Table(
   'clean_measure', meta,
   Column('station', String, primary_key=True),
   Column('date', String),
   Column('precip', String),
   Column('tobs', String)
)

clean_stations = Table(
   'clean_stations', meta,
   Column('station', String, primary_key=True),
   Column('latitude', String),
   Column('longitude', String),
   Column('elevation', String),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)

meta.create_all(engine)
# print(engine.table_names())

cleanMeasure = data_manager1.get_from_csv()
cleanStations = data_manager2.get_from_csv()
# x = cleanStations[0]
# print(type(x[0]))

for stations in cleanStations[1:]:
      ins = clean_stations.insert().values(station=stations[0], latitude=stations[1], longitude=stations[2], elevation=stations[3], name=stations[4], country=stations[5], state=stations[6] )     
      conn = engine.connect()
      result = conn.execute(ins)

for measure in cleanMeasure[1:]:
      ins = clean_measure.insert().values(station=measure[0], date=measure[1], precip=measure[2], tobs=measure[3] )     
      conn = engine.connect()
      result = conn.execute(ins)
