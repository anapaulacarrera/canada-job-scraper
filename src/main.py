from scraper import scrape_jobs
import pandas as pd

companies = [
    {
        "company": "RBC",
        "sector": "Banking",
        "url": "https://jobs.rbc.com/ca/en/search-results",
        "title_selector": ".job-title",     # <-- placeholder selectors (we will update)
        "link_selector": ".job-title a",
        "location_selector": ".job-location",
        "base_url": "https://jobs.rbc.com"
    },
    {
        "company": "TD",
        "sector": "Banking",
        "url": "https://jobs.td.com/en/job-search-results/",
        "title_selector": ".job-title",     # placeholder, will update after inspection
        "link_selector": ".job-title a",
        "location_selector": ".job-card__location",
        "base_url": "https://jobs.td.com"
    }
]

# scraping each company
all_jobs = []

for c in companies:
    print(f" Scraping {c['company']}...") # this helps you see which company the script is currently scraping

    jobs = scrape_jobs(
        url=c["url"],
        company=c["company"],
        sector=c["sector"],
        title_selector=c["title_selector"],
        link_selector=c["link_selector"],
        location_selector=c["location_selector"],
        base_url=c["base_url"]
    )

    print(f"Found {len(jobs)} jobs at {c['company']}")
    all_jobs.extend(jobs)

# converting into a df and saving as a CSV 
df = pd.DataFrame(all_jobs)

print("\n Saving results to data/jobs.csv...\n")

df.to_csv("../data/jobs.csv", index=False)

print("Your job dataset is ready.")
