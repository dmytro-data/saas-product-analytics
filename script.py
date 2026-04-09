import pandas as pd
import numpy as np
from datetime import datetime, timedelta

n_users = 1000
df_users = pd.DataFrame({
    'user_id': np.arange(1, n_users + 1),
    'region': np.random.choice(['North America', 'Europe', 'Asia'], n_users),
    'platform': np.random.choice(['iOS', 'Android', 'Web'], n_users),
    'reg_date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 200)) for _ in range(n_users)]
})

payments = []
for _, row in df_users.iterrows():
    for i in range(np.random.randint(1, 10)):
        pay_date = row['reg_date'] + timedelta(days=30 * i)
        if pay_date < datetime(2023, 12, 31):
            payments.append({'user_id': row['user_id'], 'pay_date': pay_date, 'amount': 10})

df_payments = pd.DataFrame(payments)

df_users.to_csv('raw_users.csv', index=False)
df_payments.to_csv('raw_payments.csv', index=False)