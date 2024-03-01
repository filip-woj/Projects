import pandas as pd
import numpy as np

# Import csv's
df = pd.read_csv('Nov09JnyExport.csv')
print("Row count: ")
print(len(df))
# geo = pd.read_csv('London stations.csv')

# # strip and lowercase the start station column in main df
# dff = df.copy()
# dff['StartStn'] = dff['StartStn'].str.strip().str.lower()



# # ----------------------------------------------------------------------------------
# # clean the start station column so it matches the london station df
# dff['StartStn'] = dff['StartStn'].str.replace('dlr', '') # removes 'dlr' from end of station name
# dff['StartStn'] = dff['StartStn'].str.replace('tram', '') # removes 'tram' from end of statio name
# dff['StartStn'] = dff['StartStn'].str.replace(' nr', '') # removes 'nr' from end of station name
# dff['StartStn'] = dff['StartStn'].str.replace(' e2', '') # removes 'e2' from end of station names
# dff['StartStn'] = dff['StartStn'].str.replace('&', 'and') #replaces & with 'and'
# dff['StartStn'] = dff['StartStn'].str.replace(r' nl', '') # removes 'nl' from end of station names
# dff['StartStn'] = dff['StartStn'].str.replace('qns r', 'queens road') # replaces 'qns r' in walthamstow queens road with queens road
# dff['StartStn'] = dff['StartStn'].str.replace(' jn', 'junction') #replaces 'jn' at the end of station names with junction
# dff['StartStn'] = dff['StartStn'].str.replace('wk', 'walk') #replaces 'jn' at the end of station names with junction
# dff['StartStn'] = dff['StartStn'].str.replace('pk', 'park') #replaces 'pk' at the end of station names with park
# dff['StartStn'] = dff['StartStn'].str.replace('strt', 'street') # replaces strt with street
# dff['StartStn'] = dff['StartStn'].str.replace('rdandb\'sby', 'road and barnsbury') # replaces rdandb\'sby with road and barnsbury
# dff['StartStn'] = dff['StartStn'].str.replace('blckhrs lne', 'blackhorse lane')
# dff['StartStn'] = dff['StartStn'].str.replace('blckhrs lne', 'blackhorse lane')
# dff['StartStn'] = dff['StartStn'].str.replace('term', 'terminal')
# dff['StartStn'] = dff['StartStn'].str.replace('terms', 'terminals')
# dff['StartStn'] = dff['StartStn'].str.replace('123', '1 2 3')
# dff['StartStn'] = dff['StartStn'].str.replace('hampst\'d', 'hampstead')
# dff['StartStn'] = dff['StartStn'].str.replace('tlink', 'thameslink')
# dff['StartStn'] = dff['StartStn'].str.replace('cutty sark', 'cutty sark for maritime greenwich')
# dff['StartStn'] = dff['StartStn'].str.replace('edgware road m', 'edgware road')
# dff['StartStn'] = dff['StartStn'].str.replace('edgware road b', 'edgware road')
# dff['StartStn'] = dff['StartStn'].str.replace('hammersmith m', 'hammersmith')
# dff['StartStn'] = dff['StartStn'].str.replace('hammersmith d', 'hammersmith')
# dff['StartStn'] = dff['StartStn'].str.replace('kings cross', 'kings cross st. pancras')
# dff['StartStn'] = dff['StartStn'].str.replace('high street kens', 'high street kensington')
# dff['StartStn'] = dff['StartStn'].str.replace('highbiry', 'highbury and islington')
# dff['StartStn'] = dff['StartStn'].str.replace('leytonstone high rd', 'leytonstone high road')
# dff['StartStn'] = dff['StartStn'].str.replace('waterloo jle', 'waterloo')
# dff['StartStn'] = dff['StartStn'].str.replace('bromley by bow', 'bromley-by-bow')
# dff['StartStn'] = dff['StartStn'].str.replace('fenchurch st', 'fenchurch street')
# dff['StartStn'] = dff['StartStn'].str.replace('addngtn vil', 'addington village')
# dff['StartStn'] = dff['StartStn'].str.replace('beddngtn ln', 'beddington lane')
# dff['StartStn'] = dff['StartStn'].str.replace('beckenhm rd', 'beckenham road')
# dff['StartStn'] = dff['StartStn'].str.replace('beckenhmjunction', 'beckenham junction')
# dff['StartStn'] = dff['StartStn'].str.replace('great portland st', 'great portland street')
# dff['StartStn'] = dff['StartStn'].str.replace('mitcham jcn', 'mitcham junction')
# dff['StartStn'] = dff['StartStn'].str.replace('shepherd\'s bush', 'shepherds bush')
# dff['StartStn'] = dff['StartStn'].str.replace('shepherd\'s bush mkt', 'shepherds bush market')
# dff['StartStn'] = dff['StartStn'].str.replace('shepherds bush mkt', 'shepherds bush market')
# dff['StartStn'] = dff['StartStn'].str.replace('shepherds bush und', 'shepherds bush')
# dff['StartStn'] = dff['StartStn'].str.strip()
# # ----------------------------------------------------------------------------------

# # clean the station column so it can match easily with the main df station column
# geo_copy = geo.copy()
# long_lat = geo_copy[['Station', 'Latitude', 'Longitude']]
# long_lat['Station'] = long_lat['Station'].str.strip().str.lower()

# geo_copy['Station'] = geo_copy['Station'].str.strip().str.lower().str.replace('-',' ')


# # merge the two df's on the station columns'
# merged_df = pd.merge(dff, long_lat, left_on = 'StartStn', right_on = 'Station', how = 'left')

# # remove any rows where the start station is either bus or unstarted
# filtered_df = merged_df[~merged_df['StartStn'].isin(['unstarted', 'bus'])]

# #remove any rows that don't have longitude or latitude
# filtered_df = filtered_df.dropna(subset=['Longitude', 'Latitude'])

# #save to csv
# filtered_df.to_csv('data_with_long_lat.csv', index=False)
