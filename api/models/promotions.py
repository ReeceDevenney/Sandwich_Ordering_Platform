from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(20), nullable=False)
    discount = Column(DECIMAL(2,2), nullable=False)
    isActive = Column(Boolean, nullable=False, default=True)
    expirationDate = Column(DATETIME, nullable=False)

