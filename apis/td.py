import requests
import json

TD_API = "https://td.wd3.myworkdayjobs.com/wday/cxs/td/TD_Bank_Careers/jobs"

DS_KEYWORDS = [
    "data", "analytics", "analyst", "scientist",
    "machine learning", "ml", "ai",
    "business intelligence", "bi"
]

def is_data_role(title: str) -> bool:
    t = title.lower()
    return any(k in t for k in DS_KEYWORDS)

def is_toronto(location: str) -> bool:
    return "toronto" in location.lower()

def fetch_td_jobs(limit=20, offset=0):
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
        "Origin": "https://td.wd3.myworkdayjobs.com",
        "Referer": "https://td.wd3.myworkdayjobs.com/en-US/TD_Bank_Careers"
    }

    response = requests.post(
        TD_API,
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code != 200:
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        response.raise_for_status()

    data = response.json()

    jobs = []
    for job in data.get("jobPostings", []):
        title = job.get("title", "")
        location = job.get("locationsText", "")

        # client-side filtering (robust)
        if not is_data_role(title):
            continue
        if not is_toronto(location):
            continue

        jobs.append({
            "company": "TD",
            "job_id": job.get("externalPath"),
            "title": title,
            "location": location,
            "posted_date": job.get("postedOn"),
            "category": job.get("jobFamily"),
            "url": "https://td.wd3.myworkdayjobs.com" + job.get("externalPath"),
            "source": "workday"
        })

    return jobs
