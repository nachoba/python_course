# %%
"""
# Pandas Tutorial
https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

## How do I read and write tabular data?
https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html

To start using pandas the convention is to importing `as pd`.
"""

# %%
import pandas as pd

# %%
"""
![alt text](003-data.png)

I want to analyze the Titanic passenger data, available as a CSV file.
"""

# %%
titanic = pd.read_csv('titanic.csv')
print(titanic)

# %%
"""
Pandas provides the `read_csv()` function to read data stored as a csv file into a pandas `DataFrame`.

Pandas supports many different file formats or data sources out of the box (csv, excel, sql, json,...), each of them with the prefix `read_*()`

Make sure to always have a check on the 
"""
