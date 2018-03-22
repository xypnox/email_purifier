import pandas as pd

data_df = pd.read_csv('sample.csv')

for column in data_df.columns:
    if column == 'Email':
        emails = data_df['Email']

for email in emails:
    print(email)

data_df.replace('lorem@gmail.com', 'lorem@gamil.com')

for column in data_df.columns:
    if column == 'Email':
        emails = data_df['Email']

for email in emails:
    print(email)
