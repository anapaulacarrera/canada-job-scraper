# Automated Job Scraper for Canadian Banking & Insurance Companies

This project builds an automated Python-based data ingestion pipeline that collects data-focused job postings from major Canadian banking and insurance companies using undocumented company APIs. The pipeline identifies roles such as Data Analyst, Data Scientist, and BI Analyst, and consolidates them into a unified dataset for exploratory labor-market analysis.

The goal is to reduce the time spent manually reviewing multiple company career pages and to create a centralized dataset aligned with the Toronto job market, enabling analysis of role availability, seniority distribution, and hiring trends across firms.

## Project Structure 
```
job-scraper-canada/
├── apis/
│   ├── td.py
│   ├── cibc.py
│   ├── aviva.py
│   ├── intact.py
├── run_scraper.py
├── data/
│   ├── jobs_raw.json
│   ├── jobs_raw_ndjson.json
│   └── README.md
├── docs/
│   └── report_draft.pdf
└── README.md

```
## Current Status 
- API-based ingestion implemented for multiple Canadian firms
- Modular company-specific collectors with centralized execution via run_scraper.py
- Raw job posting data consolidated into JSON and NDJSON formats
- Next phase: SQL-based querying and exploratory analysis of Toronto hiring trends

## Technologies Used
- Python 3
- requests
- pandas

## Author 
Ana Carrera

Data Science @ The University of Texas at Dallas 

Focus: machine learning, NLP, data analytics 
