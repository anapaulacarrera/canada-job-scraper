import requests
import json

AVIVA_API = "https://aviva.wd1.myworkdayjobs.com/wday/cxs/aviva/External/jobs"

DS_KEYWORDS = [
    "data", "analytics", "analyst", "scientist",
    "machine learning",
    "business intelligence", "bi",
    "model", "quant"
]

# Workday facet IDs (from browser)
CANADA_ID = "a30a87ed25634629aa6c3958aa2b91ea"
TORONTO_ID = "51f8f16388b2015a00a934356b4af085"

def is_data_role(title: str) -> bool:
    t = title.lower()
    return any(k in t for k in DS_KEYWORDS)

def fetch_aviva_jobs(limit=20, offset=0):
    payload = {
        "appliedFacets": {
            "Location_Country": [CANADA_ID],
            "locations": [TORONTO_ID]
        },
        "searchText": "",
        "limit": limit,
        "offset": offset
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://aviva.wd1.myworkdayjobs.com",
        "Referer": "https://aviva.wd1.myworkdayjobs.com/en-US/External"
    }

    response = requests.post(
        AVIVA_API,
        headers=headers,
        data=json.dumps(payload)
    )

    response.raise_for_status()
    data = response.json()

    jobs = []

    for job in data.get("jobPostings", []):
        title = job.get("title", "")

        if not is_data_role(title):
            continue

        jobs.append({
            "company": "Aviva",
            "job_id": job.get("externalPath"),
            "title": title,
            "location": job.get("locationsText"),
            "posted_date": job.get("postedOn"),
            "category": job.get("jobFamily"),
            "url": "https://aviva.wd1.myworkdayjobs.com" + job.get("externalPath"),
            "source": "workday"
        })

    return jobs
