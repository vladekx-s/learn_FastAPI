from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
#from sqlalchemy.orm import sessionmaker
from core.settings import setting

class DB_HELPER:
    def __init__(self):
        self.engine = create_async_engine(
            url = setting.urlDB,
            echo = True
        )

        self.session = async_sessionmaker(
            bind = self.engine,
            autoflush = False,
            autocommit = False,
            expire_on_commit = False
        )

db_helper_obj = DB_HELPER()