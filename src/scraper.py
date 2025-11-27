import requests # lets you load a webpage the same way a browser does
from bs4 import BeautifulSoup # lets you search through HTML 

def scrape_jobs(url, company, sector, title_selector, link_selector,
                location_selector=None, base_url=None):

    # sending HTTP request to the website
    headers = {"User-Agent": "Mozilla/5.0"}  # protects you from simple blocking
    response = requests.get(url, headers=headers) 

    # if the website doesn't load, stop early and return empty list
    if response.status_code != 200:
        print(f"Failed to fetch {company} page — status code:", response.status_code)
        return []

    # feeding the raw html to BeautifulSoup to turn it into a structured object
    soup = BeautifulSoup(response.text, "lxml") # lxml is the parser, the engine to interpret the HTML

    # finding elements that match the given CSS selectors
    titles = soup.select(title_selector)
    links = soup.select(link_selector)
    locations = soup.select(location_selector) if location_selector else []

    jobs = []

    # looping through all jobs found
    for i in range(len(titles)):
        
        # extracting job title text
        title = titles[i].get_text(strip=True)

        # extracting job link
        if i < len(links):
            link = links[i].get("href")

            # if the link is relative, add the base URL
            if link and base_url and not link.startswith("http"):
                link = base_url + link
        else:
            link = None  # fallback if no link detected

        # extracting location 
        if location_selector:
            if i < len(locations):
                location = locations[i].get_text(strip=True)
            else:
                location = ""
        else:
            location = ""

        # adding job dictionary to the list
        jobs.append({
            "title": title,
            "company": company,
            "sector": sector,
            "location": location,
            "url": link
        })

    return jobs
