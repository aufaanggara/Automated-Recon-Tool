from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./recon.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class ScanResult(Base):
    __tablename__ = "scan_results"
    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String)
    scan_time = Column(DateTime, default=datetime.utcnow)
    subdomains = Column(Text)
    live_hosts = Column(Text)
    nmap_result = Column(Text)
    whois_result = Column(Text)


def init_db():
    Base.metadata.create_all(bind=engine)
