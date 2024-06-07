from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Parroquia, Provincia
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

provincias = session.query(Provincia).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Nùmero de establecimientos por parroquia")
for s in provincias:
    print("%s" % (s))
    print("---------")
    print("%s" % (s.obtener_lista_parroquias())) #Se le esta poniendo la resposabilidad al objeto
    print("---------")