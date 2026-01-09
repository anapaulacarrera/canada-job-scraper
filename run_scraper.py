from apis.td import fetch_td_jobs
from apis.cibc import fetch_cibc_jobs
from apis.aviva import fetch_aviva_jobs
import json

def main():
    all_jobs = []

    # ---------- TD ----------
    td_jobs = []
    for offset in range(0, 300, 20):
        batch = fetch_td_jobs(limit=20, offset=offset)
        if not batch:
            break
        td_jobs.extend(batch)

    print(f"TD jobs: {len(td_jobs)}")
    all_jobs.extend(td_jobs)

    # ---------- CIBC ----------
    cibc_jobs = []
    for offset in range(0, 300, 20):
        batch = fetch_cibc_jobs(limit=20, offset=offset)
        if not batch:
            break
        cibc_jobs.extend(batch)

    print(f"CIBC jobs: {len(cibc_jobs)}")
    all_jobs.extend(cibc_jobs)

    # ---------- AVIVA ----------
    aviva_jobs = []
    for offset in range(0, 200, 20):
        batch = fetch_aviva_jobs(limit=20, offset=offset)
        if not batch:
            break
        aviva_jobs.extend(batch)

    print(f"Aviva jobs: {len(aviva_jobs)}")
    all_jobs.extend(aviva_jobs)

    # ---------- SAVE ----------
    with open("data/jobs_raw.json", "w") as f:
        json.dump(all_jobs, f, indent=2)

    print(f"\nTotal jobs saved: {len(all_jobs)}")
    print("Saved to data/jobs_raw.json")

if __name__ == "__main__":
    main()
