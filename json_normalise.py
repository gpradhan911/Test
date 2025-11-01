
import pandas as pd
from IPython.core.display_functions import display
from pandas import json_normalize
import json
import numpy as np
import requests

# #simple list with nested dictionary
#
# data_list = [
#     {"id": 1, "user": {"name": "Bob", "email": "bob@example.com"}},
#     {"id": 2, "user": {"name": "Charlie", "email": "charlie@example.com"}}
# ]
#
# df=pd.json_normalize(data_list)
# print(df)

#complex list data with nested dictionary and list inside

# complex_data= {
#     "company": "TechCorp",
#     "employees": [
#         {"id": 101, "name": "David", "skills": ["Python", "SQL"]},
#         {"id": 102, "name": "Eve", "skills": ["Java", "Cloud"]}
#     ],
#     "location": "San Francisco",
#     "group" : "humanresource",
#     "department": {"head": "Director","name":"roy su"}
#     # max flatten upto department_head or department_name
# }
#
# df2=pd.json_normalize(complex_data,record_path=["employees"], max_level=None,sep="_",meta=['company','location','group',['department',"head"]])
# display(df2)
# #

#complex_data 2
data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]
df3 =pd.json_normalize(data,record_path=['counties'],meta=['state','shortname',['info','governor']],sep='_',max_level=None)
print(df3)