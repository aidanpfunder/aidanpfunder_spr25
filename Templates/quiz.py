import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv'
df = pd.read_csv(url)

# Filter for babies named 'Oliver' and sum the births for all years
oliver_babies = df[df['name'] == 'Oliver']
total_oliver_babies = oliver_babies['births'].sum()

print(f"Total number of babies named Oliver: {total_oliver_babies}")