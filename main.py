from sqlalchemy import Table, Column, Integer, String, MetaData, Date, Float
from sqlalchemy import create_engine
from data_manager.data_manager import data_manager

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

clean_measure = Table(
   'clean_measure', meta,
   Column('station', Integer, primary_key=True),
   Column('date', Date),
   Column('precip', Float),
   Column('tobs', Integer)
)

meta.create_all(engine)
print(engine.table_names())

cleanMeasure = data_manager.get_from_csv()


for measure in cleanMeasure[1:]:
    ins = clean_measure.insert()
    ins = clean_measure.insert().values(station=measure[0], date=measure[1], precip=measure[2], tobs=measure[3] )
    conn = engine.connect()
    result = conn.execute(ins)
    conn.execute(ins, [
    {'station': measure[0], 'date': measure[1], 'precip':measure[2], 'tobs': measure[3] }
    ])


