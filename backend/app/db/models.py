from sqlalchemy import Column, Integer, String, JSON
from app.db.base import Base

class SEOReport(Base):
    __tablename__ = "seo_reports"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False, index=True)
    score = Column(Integer, nullable=False)
    metrics = Column(JSON, nullable=False)
    ai_summary = Column(String, nullable=False)
    ai_suggestions = Column(JSON, nullable=False)
