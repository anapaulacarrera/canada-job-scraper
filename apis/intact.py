import requests

INTACT_API = "https://careers.intactfc.com/api/get-jobs"

DATA_POSITIVE = [
    "data analyst",
    "data scientist",
    "analytics",
    "business intelligence",
    "bi ",
    "machine learning",
    "ml ",
    "artificial intelligence",
    "ai ",
    "quantitative",
    "modeling",
    "insights"
]

DATA_NEGATIVE = [
    "claims",
    "adjuster",
    "technician",
    "mechanic",
    "prep",
    "repair",
    "autocare",
    "call centre",
    "customer",
    "sales",
    "broker",
    "specialist"
]

def is_data_role(title: str) -> bool:
    t = title.lower()
    if not any(k in t for k in DATA_POSITIVE):
        return False
    if any(bad in t for bad in DATA_NEGATIVE):
        return False
    return True

def is_toronto(location: str) -> bool:
    if not location:
        return False
    l = location.lower()
    return "toronto" in l or "ontario" in l

def fetch_intact_jobs(page_number=1):
    params = {
        "radius": 15,
        "page_number": page_number,
        "enable_kilometers": "true"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Origin": "https://careers.intactfc.com",
        "Referer": "https://careers.intactfc.com/"
    }

    response = requests.get(
        INTACT_API,
        params=params,
        headers=headers
    )

    response.raise_for_status()
    data = response.json()

    jobs_raw = data.get("jobs", [])
    jobs = []

    for job in jobs_raw:
        title = job.get("title", "")
        location = job.get("location", "")

        if not is_data_role(title):
            continue
        if not is_toronto(location):
            continue

        jobs.append({
            "company": "Intact",
            "job_id": job.get("job_id"),
            "title": title,
            "location": location,
            "posted_date": job.get("posted_date"),
            "category": job.get("category"),
            "url": job.get("job_url"),
            "source": "intact_api"
        })

    return jobs
