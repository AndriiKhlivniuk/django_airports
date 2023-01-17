from celery import shared_task
import pandas as pd
from .models import Airport

@shared_task
def add_csv_data():
    url = 'https://davidmegginson.github.io/ourairports-data/airports.csv'
    df = pd.read_csv(url)
    print(df.keys())

    for i, row in df.iterrows():

        if not row.elevation_ft.is_integer():
            row.elevation_ft = None

        updated_values = dict(
            ident = row.ident, type = row.type, name = row['name'], 
            latitude_deg= row.latitude_deg, longitude_deg = row.longitude_deg, 
            elevation_ft = row.elevation_ft, continent = row.continent,
            iso_country = row.iso_country, iso_region = row.iso_region,
            municipality = row.municipality, scheduled_service = row.scheduled_service,
            gps_code=row.gps_code, iata_code = row.iata_code, local_code = row.local_code,
            home_link = row.home_link, wikipedia_link=row.wikipedia_link,
            keywords = row.keywords)

        Airport.objects.update_or_create(id = row.id, defaults = updated_values)
        

