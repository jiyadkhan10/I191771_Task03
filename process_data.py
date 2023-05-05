import pandas as pd
from sklearn.preprocessing import LabelEncoder

# load the dataset
df = pd.read_csv('data.csv')

# drop unnecessary columns
df = df.drop(['tourney_level', 'match_num', 'winner_id', 'winner_seed', 'winner_entry',
              'winner_hand', 'winner_ht', 'loser_id', 'loser_seed', 'loser_entry',
              'loser_hand', 'loser_ht', 'score'], axis=1)

# convert date to datetime object
df['tourney_date'] = pd.to_datetime(df['tourney_date'], format='%Y%m%d')

# label encode categorical variables
label_encoder = LabelEncoder()
df['tourney_name'] = label_encoder.fit_transform(df['tourney_name'])
df['surface'] = label_encoder.fit_transform(df['surface'])
df['round'] = label_encoder.fit_transform(df['round'])

# drop rows with missing values
df = df.dropna()

# display the first 5 rows of the pre-processed dataset
print(df.head())

df.to_csv("data_processed.csv")
