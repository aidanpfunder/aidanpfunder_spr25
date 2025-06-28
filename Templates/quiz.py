import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dwellings_ml dataset
df = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")

# Split into features (X) and target (y)
X = df.drop(columns=['before1980'])
y = df['before1980']

# Create training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.34, random_state=76)

# Calculate average of the first 10 selling prices in training set
average_sprice = X_train['sprice'].head(10).mean()

print("Average of the first 10 sprice values in X_train:", average_sprice)
