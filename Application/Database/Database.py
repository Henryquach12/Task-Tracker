from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Henry1209@localhost:3306/usersdb"

#Connect to MySQL
engine = create_engine(
    DATABASE_URL,
    echo=True, 
    future=True
)

#Session to work with database
SessionLocal = sessionmaker(
    bind=engine, # attach this session factory to the MySQL engine
    autoflush=False, # prevent auto-flush; control when data is sent to DB
    autocommit=False 
    )

#Use to declare SQL table
Base = declarative_base()



