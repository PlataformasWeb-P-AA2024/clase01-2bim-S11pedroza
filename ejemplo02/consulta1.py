from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Canton, Parroquia
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

cantones = session.query(Canton).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Nùmero de estudiantes por canton")
for s in cantones:
    print("%s" % (s))
    print("---------")
    print("%s" % (s.obtener_num_estudiantes_canton())) #Se le esta poniendo la resposabilidad al objeto
    print("---------")

