import pandas as pd

from nba_api.stats.endpoints import playercareerstats

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
df = career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()

print(df.head())
