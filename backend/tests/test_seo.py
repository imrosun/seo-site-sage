from app.core.seo import compute_seo_score

def test_seo_score_perfect():
    metrics = {
        "title": "Test",
        "h1_count": 1,
        "images_missing_alt": 0,
        "load_time_ms": 1000,
    }
    assert compute_seo_score(metrics) == 100
