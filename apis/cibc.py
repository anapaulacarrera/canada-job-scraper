import requests
import json

CIBC_API = "https://cibc.wd3.myworkdayjobs.com/wday/cxs/cibc/search/jobs"

DS_KEYWORDS = [
    "data", "analytics", "analyst", "scientist",
    "machine learning", "ai",
    "business intelligence", "bi",
    "model", "quant", "risk"
]

def is_data_role(title: str) -> bool:
    t = title.lower()
    return any(k in t for k in DS_KEYWORDS)

def is_toronto(location: str) -> bool:
    if not location:
        return False
    return "toronto" in location.lower()

def fetch_cibc_jobs(limit=20, offset=0):
    payload = {
        "appliedFacets": {},
        "searchText": "data analytics",
        "limit": limit,
        "offset": offset
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://cibc.wd3.myworkdayjobs.com",
        "Referer": "https://cibc.wd3.myworkdayjobs.com/en-US/search"
    }

    response = requests.post(
        CIBC_API,
        headers=headers,
        data=json.dumps(payload)
    )

    response.raise_for_status()
    data = response.json()

    jobs = []

    for job in data.get("jobPostings", []):
        title = job.get("title", "")
        location = job.get("locationsText", "")

        if not is_data_role(title):
            continue
        if not is_toronto(location):
            continue

        jobs.append({
            "company": "CIBC",
            "job_id": job.get("externalPath"),
            "title": title,
            "location": location,
            "posted_date": job.get("postedOn"),
            "category": job.get("jobFamily"),
            "url": "https://cibc.wd3.myworkdayjobs.com" + job.get("externalPath"),
            "source": "workday"
        })

    return jobs
