SELECT
  company,
  COUNT(*) AS december_postings
FROM (
  SELECT DISTINCT job_id, company
  FROM raw
)
GROUP BY company
ORDER BY december_postings DESC;
