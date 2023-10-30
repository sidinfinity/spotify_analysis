import pandas as pd
import sys
import os

# making this a function so I can use this in main.ipynb
def load_data():
    csv_path = os.path.join(os.getcwd(), "spotify.csv")
    df = pd.read_csv(csv_path, encoding='ISO-8859-1')

    # any data preprocessing goes here

    return df