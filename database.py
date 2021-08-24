import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import constants
import pymysql
import paramiko
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder



engine = create_engine(constants.SQLALCHEMY_DATABASE_URL, echo=False,
                       pool_recycle=1800, pool_timeout=20, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# server = SSHTunnelForwarder(
#      ('23.96.93.197', 22),
#      ssh_username="azureuser",
#      ssh_private_key=r'mysql1',
#      remote_bind_address=('localhost', 3306)
# )
# server.start()
# engine = create_engine(
#     f'mysql+mysqldb://root:admin@localhost:{server.local_bind_port}/ab_in_dev_v5?charset=utf8',echo=False, pool_recycle=1800, pool_timeout=20, pool_pre_ping=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()



