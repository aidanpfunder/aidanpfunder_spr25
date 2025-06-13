
# Read in libraries
import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html(isolated_frame=True)
df = pd.read_json("https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json")

# If your missing months are true NaNs:
num_missing = df['month'].isna().sum()

# If some entries literally contain the string "n/a" (any case):
num_na_strings = df['month'].astype(str).str.lower().eq('n/a').sum()

# Combine both checks:
mask = df['month'].isna() | df['month'].astype(str).str.lower().eq('n/a')
total_na = mask.sum()

print(f"Missing (NaN) months: {num_missing}")
print(f"Literal 'n/a' months:    {num_na_strings}")
print(f"Total n/a or missing:    {total_na}")

na_counts = df.isna().sum()
print(na_counts[na_counts == 23])
