SELECT 
    p.user_id,
    p.pay_date,
    p.amount,
    u.region,
    u.platform,
    MIN(p.pay_date) OVER (PARTITION BY p.user_id) AS cohort_month,
    (strftime('%Y', p.pay_date) - strftime('%Y', MIN(p.pay_date) OVER (PARTITION BY p.user_id))) * 12 +
    (strftime('%m', p.pay_date) - strftime('%m', MIN(p.pay_date) OVER (PARTITION BY p.user_id))) AS cohort_index
FROM raw_payments p
JOIN raw_users u ON p.user_id = u.user_id;
