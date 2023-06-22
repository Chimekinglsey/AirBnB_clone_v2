from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from models.state import Base
from os import getenv


class DBStorage:
    """Class created for sql storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance of the class DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        url = "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database)
        self.__engine = create_engine(url, pool_pre_ping=True)
        #self.__engine.connect()

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Session creation"""
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        my_dict = {}
        self.__session = Session()
        if cls is None:
            for attributes in classes:
                get = self.__session.query(attributes).all()
                for i in get:
                    print(i)
            else:
                self.__session.query(cls).all()


chk = DBStorage()
chk.all('User')