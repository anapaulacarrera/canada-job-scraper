import json

with open("data/jobs_raw.json", "r") as f:
    data = json.load(f)

with open("data/jobs_raw_ndjson.json", "w") as f:
    for record in data:
        f.write(json.dumps(record) + "\n")
