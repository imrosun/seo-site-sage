from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.seo import AuditRequest, AuditResponse
from app.db.session import SessionLocal
from app.db.models import SEOReport
from app.core.crawler import crawl_url
from app.core.seo import compute_seo_score
from app.core.ai import generate_ai_insights
from urllib.parse import urlparse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and parsed.netloc

@router.post("/audit", response_model=AuditResponse)
async def audit_sites(payload: AuditRequest, db: Session = Depends(get_db)):
    if not payload.urls:
        raise HTTPException(status_code=400, detail="No URLs provided")

    reports = []

    for url in payload.urls:
        if not is_valid_url(url):
            reports.append({
                "url": url,
                "seo_score": 0,
                "metrics": {},
                "ai_summary": "Invalid URL format",
                "ai_suggestions": ["Provide a valid http or https URL"],
            })
            continue

        try:
            metrics = await crawl_url(url)
            score = compute_seo_score(metrics)
            summary, suggestions = generate_ai_insights(metrics)

            db.add(SEOReport(
                url=url,
                score=score,
                metrics=metrics,
                ai_summary=summary,
                ai_suggestions=suggestions,
            ))
            db.commit()

            reports.append({
                "url": url,
                "seo_score": score,
                "metrics": metrics,
                "ai_summary": summary,
                "ai_suggestions": suggestions,
            })

        except Exception as e:
            reports.append({
                "url": url,
                "seo_score": 0,
                "metrics": {},
                "ai_summary": "Failed to analyze URL",
                "ai_suggestions": [str(e)],
            })

    return {"status": "completed", "reports": reports}
