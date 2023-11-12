from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Use w/ Postgres
SQLALCHEMY_DATABASE_URL = "postgresql://biifaltj:aFBCMZf31JloGtzBn8u-YEQSRK-Y5kLZ@suleiman.db.elephantsql.com/biifaltj"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)




# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
