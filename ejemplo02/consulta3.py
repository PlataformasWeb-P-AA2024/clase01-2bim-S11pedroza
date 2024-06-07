from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Parroquia, Establecimiento
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

parroquias = session.query(Parroquia).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Nùmero de establecimientos por parroquia")
for s in parroquias:
    print("%s" % (s))
    print("---------")
    print("Establecimientos:" "%s" % (s.obtener_num_establecimientos_parroquia())) #Se le esta poniendo la resposabilidad al objeto
    print("---------")