import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from datetime import datetime
import matplotlib.ticker as mtick
import requests
import json
import config
# frames = df.to_dict()

response = requests.request("GET", config.myUrl, headers=config.headers, data = config.payload)
myData = response.json()['data']
""""
for key, value in myData['lifetime']['all']['properties'].items():
    print (key,value)
"""
df = pd.DataFrame(myData['lifetime']['all']['properties'].items())
print(df)
