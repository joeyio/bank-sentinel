'''
api from https://banks.data.fdic.gov/docs/#/Structure/searchInstitutions

based on work from
https://doi.org/10.1016/j.ribaf.2017.07.104 - Predicting bank failure: An improvement by implementing a machine-learning approach to classical financial ratios
https://doi.org/10.1016/j.dss.2012.11.015 - Partial Least Square Discriminant Analysis for bankruptcy prediction
https://doi.org/10.1016/j.eswa.2008.01.053 - Effects of feature construction on classification performance: An empirical study in bank failure prediction

'''

import requests
import pandas as pd
from io import StringIO

response = requests.get('https://banks.data.fdic.gov/api/institutions?' +
                        'filters=STALP%3ACA%20AND%20ACTIVE%3A0&' +
                        'fields=NAME%2CZIP%2COFFDOM%2CCITY%2CSTNAME%2CSTALP%2CNAME%2CACTIVE%2CCBSA%2CASSET%2CNETINC%2CDEP%2CDEPDOM%2CROE%2CROA%2CDATEUPDT%2COFFICES&' +
                        'sort_by=OFFICES&sort_order=DESC&limit=1000&offset=0&format=csv&download=false&filename=data_file')
data = response.text

response2 = requests.get('https://banks.data.fdic.gov/api/institutions?search=NAME%3A%20Silicon%20Valley&fields=NAME%2CZIP%2COFFDOM%2CCITY%2CSTNAME%2CSTALP%2CNAME%2CACTIVE%2CCBSA%2CASSET%2CNETINC%2CDEP%2CDEPDOM%2CROE%2CROA%2CDATEUPDT%2COFFICES&sort_by=OFFICES&sort_order=DESC&limit=10&offset=0&format=csv&download=false&filename=data_file')
data2 = response2.text

df = pd.read_csv(StringIO(data))
print(df)