title = '2023 Top 3 Legendaries Each Month'

sqlStr = '''
WITH MonthlyTopCards AS (
  SELECT
    strftime('%Y-%m', timestamp, 'unixepoch') AS month_year,
    card_name,
    season,
    SUM(price) AS total_money_moved,
    ROW_NUMBER() OVER (PARTITION BY strftime('%Y-%m', timestamp, 'unixepoch') ORDER BY SUM(price) DESC) AS rn
  FROM trades
  WHERE timestamp >= strftime('%s', '2023-01-01 00:00:00')
    AND timestamp < strftime('%s', '2024-01-01 00:00:00')
	AND CATEGORY = 'l'
  GROUP BY month_year, card_name, season
)

SELECT month_year, card_name, season, total_money_moved
FROM MonthlyTopCards
WHERE rn <= 3
ORDER BY month_year, total_money_moved DESC;
'''

def render_md(title, sql):
    return f'''
<details>
    <summary>{title}</summary>

```sql{sql}```

</details>
'''

print(render_md(title, sqlStr))