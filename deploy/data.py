import pandas as pd

# read in data
drs = "C:/Users/benno/OneDrive/Python/Dash/Deployment_ready/uber/deploy/assets/data/"
file0 = "uber_cleaned1.csv"
file1 = "uber_cleaned3.csv"

uber_df1 = pd.read_csv("".join([drs, file0]))
uber_df3 = pd.read_csv("".join([drs, file1]))