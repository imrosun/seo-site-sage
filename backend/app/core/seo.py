def compute_seo_score(metrics: dict) -> int:
    score = 100

    if not metrics["title"]:
        score -= 20

    if metrics["h1_count"] == 0:
        score -= 15
    elif metrics["h1_count"] > 1:
        score -= 10

    score -= metrics["images_missing_alt"] * 5

    if metrics["load_time_ms"] > 3000:
        score -= 15

    return max(score, 0)
