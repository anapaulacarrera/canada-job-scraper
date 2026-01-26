SELECT
  company,
  COUNT(DISTINCT title) AS unique_titles,
  COUNT(*) AS total_postings
FROM (
  SELECT DISTINCT job_id, company, title
  FROM raw
)
GROUP BY company
ORDER BY unique_titles DESC;
