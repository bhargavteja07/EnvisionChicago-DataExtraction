from sodapy import Socrata
import pandas as pd
import os

app_token = "z1tL927v10YnQHJqDeabcOw4U"
file_name = 'crime.csv'
client = Socrata("data.cityofchicago.org", app_token)
blocks = ['004XX S FINANCIAL PL',
          '002XX S CANAL ST',
          '000XX E WACKER DR',
          '001XX N CLINTON ST',
          '001XX S STATE ST',
          '006XX W RANDOLPH ST',
          '008XX S MICHIGAN AVE',
          '000XX W ADAMS ST',
          '001XX S MICHIGAN AVE',
          '000XX S LA SALLE ST',
          '002XX W MONROE ST',
          '001XX W VAN BUREN ST',
          '001XX W RANDOLPH ST',
          '000XX E LAKE ST',
          '001XX N DEARBORN ST',
          '001XX N WELLS ST',
          '001XX S RIVERSIDE PLZ',
          '001XX W RANDOLPH ST',
          '002XX N MICHIGAN AVE',
          '001XX W MADISON ST',
          '003XX S CANAL ST',
          '000XX W MONROE ST',
          '000XX E ADAMS ST',
          '001XX S LA SALLE ST',
          '006XX S WABASH AVE',
          '000XX E JACKSON BLVD',
          '006XX S DEARBORN ST',
          '002XX N CLARK ST',
          '000XX N WELLS ST',
          '001XX S WACKER DR',
          '003XX N LEAVITT ST',
          '001XX W ADAMS ST',
          '004XX S WABASH AVE',
          '001XX N FRANKLIN ST',
          '000XX N DEARBORN ST',
          '002XX S WACKER DR',
          '011XX S WABASH AVE',
          '014XX S MICHIGAN AVE',
          '001XX E RANDOLPH ST',
          '006XX S WABASH AVE']
flag = 0
for x in range(len(blocks)):
    results = client.get("6zsd-86xi", block=blocks[x], limit=6576908)
    results_df = pd.DataFrame.from_records(results)
    c = x+1
    results_df.insert(0, 'Group ID', c)
    if results_df.size != 0:
        results_df = results_df.drop('arrest', 1)
        results_df = results_df.drop('beat', 1)
        results_df = results_df.drop('community_area', 1)
        results_df = results_df.drop('description', 1)
        results_df = results_df.drop('district', 1)
        results_df = results_df.drop('domestic', 1)
        results_df = results_df.drop('fbi_code', 1)
        results_df = results_df.drop('iucr', 1)
        results_df = results_df.drop('latitude', 1)
        results_df = results_df.drop('location', 1)
        results_df = results_df.drop('location_description', 1)
        results_df = results_df.drop('longitude', 1)
        results_df = results_df.drop('updated_on', 1)
        results_df = results_df.drop('ward', 1)
        results_df = results_df.drop('x_coordinate', 1)
        results_df = results_df.drop('y_coordinate', 1)
        results_df = results_df.drop('year', 1)
        if not flag:
            results_df.to_csv(file_name)
            flag = 1
        else:
            results_df.to_csv(file_name, mode='a', header=False)
