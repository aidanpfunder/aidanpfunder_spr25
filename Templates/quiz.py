
# %%
# Read in libraries
import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html(isolated_frame=True)

# %%
# Load the CSV from the URL
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

# %%
# Strip column names for cleaner reference
df.columns = df.columns.str.strip()

# %%
# Column that indicates if they've seen any Star Wars films
col = "Have you seen any of the 6 films in the Star Wars franchise?"

# Calculate percentage
seen_yes = df[col].str.strip().eq("Yes").sum()
total_responses = df[col].notna().sum()
percentage = (seen_yes / total_responses) * 100

# Output result
print(f"Percentage of people who have seen at least one film: {percentage}%")

# %%
# Strip column names just in case
df.columns = df.columns.str.strip()

# Column names
seen_col = "Have you seen any of the 6 films in the Star Wars franchise?"
gender_col = "Gender"

# Filter only rows where gender is Male and gender is not null
males = df[df[gender_col].str.strip() == "Male"]

# Among males, how many have seen at least one film?
males_seen_yes = males[seen_col].str.strip().eq("Yes").sum()

# Total number of valid male responses (excluding nulls in 'seen_col')
total_males = males[seen_col].notna().sum()

# Calculate percentage
male_seen_pct = (males_seen_yes / total_males) * 100

print(f"Percentage of males who have seen at least one film: {male_seen_pct}%")
