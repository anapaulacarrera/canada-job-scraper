SELECT COUNT(*) AS total_unique_postings
FROM (
  SELECT DISTINCT job_id
  FROM raw
);
