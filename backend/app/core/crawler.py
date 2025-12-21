import aiohttp
from bs4 import BeautifulSoup
import time

async def crawl_url(url: str) -> dict:
    start = time.time()

    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=20) as response:
            html = await response.text()

    load_time = int((time.time() - start) * 1000)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string.strip() if soup.title else ""
    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all("h2")
    images = soup.find_all("img")

    missing_alt = len([img for img in images if not img.get("alt")])

    return {
        "title": title,
        "h1_count": len(h1_tags),
        "h2_count": len(h2_tags),
        "images_missing_alt": missing_alt,
        "load_time_ms": load_time,
    }
