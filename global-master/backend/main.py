from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 데이터베이스 설정
DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/carr"

# SQLAlchemy 엔진 및 세션 설정
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI 인스턴스 생성
app = FastAPI()

# 데이터베이스 모델 정의
class CarrTree(Base):
    __tablename__ = "carr_tree"
    no = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False)
    position = Column(String(45), nullable=False)
    summary = Column(Text, nullable=False)
    photo = Column(LargeBinary, nullable=True)
    link = Column(String(45), nullable=False)

# Pydantic 스키마 정의
class CarrTreeSchema(BaseModel):
    no: int
    name: str
    position: str
    summary: str
    photo: bytes = None
    link: str

    class Config:
        orm_mode = True

# 의존성 주입: 데이터베이스 세션 관리
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 데이터베이스에서 모든 항목을 가져오는 엔드포인트
@app.get("/carr_tree", response_model=List[CarrTreeSchema])
def read_carr_tree(db: Session = Depends(get_db)):
    items = db.query(CarrTree).all()
    return items

# 특정 항목을 ID로 조회하는 엔드포인트
@app.get("/carr_tree/{item_id}", response_model=CarrTreeSchema)
def read_carr_tree_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(CarrTree).filter(CarrTree.no == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
