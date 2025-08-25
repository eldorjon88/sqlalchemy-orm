from sqlalchemy import (
    create_engine,
    URL,
    MetaData,
)
from sqlalchemy.orm import sessionmaker

import config

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

engine = create_engine(DATABASE_URL)

Base = MetaData()

Session = sessionmaker(engine)
