from django.db import models

# Create your models here.
class Airport(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    ident = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    latitude_deg = models.FloatField(blank = True, default = 0)
    longitude_deg = models.FloatField(blank = True, default = 0)
    elevation_ft = models.IntegerField(blank = True, default = None, null = True)
    continent = models.CharField(max_length = 100, blank = True, default = "")
    iso_country = models.CharField(max_length = 100, blank = True, default = "")
    iso_region = models.CharField(max_length = 100, blank = True, default = "")
    municipality = models.CharField(max_length = 100, blank = True, default = "")
    scheduled_service = models.CharField(max_length = 100, blank = True, default = "")
    gps_code = models.CharField(max_length = 100, blank = True, default = "")
    iata_code = models.CharField(max_length = 100, blank = True, default = "")
    local_code = models.CharField(max_length = 100, blank = True, default = "")
    home_link = models.URLField(blank = True, default = "")
    wikipedia_link = models.URLField(blank = True, default = "")
    keywords = models.CharField(max_length = 100, blank = True, default = "")

    def __str__(self):
        return self.name