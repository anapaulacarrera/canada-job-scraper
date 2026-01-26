SELECT
  company,
  seniority_level,
  COUNT(*) AS postings
FROM (
  SELECT DISTINCT
    company,
    job_id,
    CASE
      WHEN LOWER(title) LIKE '%intern%'
        OR LOWER(title) LIKE '%co-op%'
        OR LOWER(title) LIKE '%coop%'
        THEN 'Student / Intern'

      WHEN LOWER(title) LIKE '%manager%'
        OR LOWER(title) LIKE '%director%'
        OR LOWER(title) LIKE '%head%'
        THEN 'Manager'

      WHEN LOWER(title) LIKE '%senior%'
        OR LOWER(title) LIKE '%sr%'
        OR LOWER(title) LIKE '%lead%'
        OR LOWER(title) LIKE '%principal%'
        THEN 'Senior'

      WHEN LOWER(title) LIKE '%analyst%'
        OR LOWER(title) LIKE '%scientist%'
        OR LOWER(title) LIKE '%engineer%'
        OR LOWER(title) LIKE '%developer%'
        THEN 'Entry-level'

      ELSE 'Mid-level'
    END AS seniority_level
  FROM raw
)
GROUP BY company, seniority_level
ORDER BY company, postings DESC;
