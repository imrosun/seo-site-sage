from pydantic import BaseModel
from typing import List, Dict

class AuditRequest(BaseModel):
    urls: List[str]

class SEOReportResponse(BaseModel):
    url: str
    seo_score: int
    metrics: Dict
    ai_summary: str
    ai_suggestions: List[str]

class AuditResponse(BaseModel):
    status: str
    reports: List[SEOReportResponse]
