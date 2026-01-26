SELECT DISTINCT
  company,
  job_id,
  title,
  CASE
    -- student roles first
    WHEN LOWER(title) LIKE '%intern%'
      OR LOWER(title) LIKE '%co-op%'
      OR LOWER(title) LIKE '%coop%'
      THEN 'Student / Intern'

    -- management before senior IC
    WHEN LOWER(title) LIKE '%manager%'
      OR LOWER(title) LIKE '%director%'
      OR LOWER(title) LIKE '%head%'
      THEN 'Manager'

    -- senior IC / leadership
    WHEN LOWER(title) LIKE '%senior%'
      OR LOWER(title) LIKE '%sr%'
      OR LOWER(title) LIKE '%lead%'
      OR LOWER(title) LIKE '%principal%'
      THEN 'Senior'

    -- entry-level full-time
    WHEN LOWER(title) LIKE '%analyst%'
      OR LOWER(title) LIKE '%scientist%'
      OR LOWER(title) LIKE '%engineer%'
      OR LOWER(title) LIKE '%developer%'
      THEN 'Entry-level'

    -- everything else
    ELSE 'Mid-level'
  END AS seniority_level
FROM raw;
