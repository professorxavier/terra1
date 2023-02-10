import pandas as pd
from utils import remove_emojis
from utils import remove_mentions
from utils import remove_stops

df = pd.read_csv("data.csv", encoding="utf-8")

df["cleaned"] = df["tweet"].apply(remove_mentions)
df["cleaned"] = df["cleaned"].apply(remove_emojis)
df["cleaned"] = df["cleaned"].apply(remove_stops)

df.to_csv("data_cleaned.csv")
