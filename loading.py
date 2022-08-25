import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import sqlite3

class Loading:
    def __init__(self, df: pd.DataFrame):
        print("Loading")
        self.DATABASE_LOCATION = "sqlite:///football.sqlite"

        self.matches_to_csv(df)
        self.matches_to_db(df)
        
    def matches_to_csv(self, df: pd.DataFrame) -> None:
        df.to_csv("matches.csv")

    def matches_to_db(self, df: pd.DataFrame) -> None:
        engine = sqlalchemy.create_engine(self.DATABASE_LOCATION)
        conn = sqlite3.connect('football.sqlite')
        cursor = conn.cursor()

        try:
            df.to_sql("matches", engine, index=False, if_exists='append')
        except:
            print("Data already exists in the database")

        conn.close()
        print("Close database successfully")