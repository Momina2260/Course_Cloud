from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
engine=create_engine('mysql+pymysql://root:Root%402003@localhost:3306/project_db',echo=True)
Base=declarative_base()