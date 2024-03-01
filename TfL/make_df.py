df = pd.read_csv('data_with_long_lat.csv')
df.columns = [col.lower() for col in df.columns]



df.rename(columns = {'downo' : 'day num'}, inplace=True)
df.rename(columns = {'daytype' : 'day'}, inplace=True)
df.rename(columns = {'downo' : 'day of week'}, inplace=True)
df.rename(columns = {'jnytyp' : 'jny type'}, inplace=True)



# Get unique station names
xstations = df['startstn'].unique()

# Create a dictionary to map station names to their string representations
station_dict = {str(station): station for station in xstations}

# Create a list of dictionaries for dropdown options
station_dropdown = [{'label': key.strip().title(), 'value': value} for key, value in station_dict.items()]

