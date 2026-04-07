import uuid
from django.db import models

"""
create table if not exists categoires(
id integer primary key autoincrement,
name varchar(255) not null unique...);
"""

#ORM 

#main_homeslider - main application (app) - main/models.py

class HomesSlider(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4) #primary key for the model
    image = models.ImageField(upload_to="home/slider/" ,verbose_name="foto") #media/slider/image_name.png | verbose_name="foto" - a name for the field in the admin panel

    def __str__(self): #string representation of the model - how the model will be displayed in the admin panel
        return f"Fotka c ID:{self.id}"


    class Meta:
        verbose_name = "foto claydera" #ilk tablo(tekil) adı / a table name in singular form
        verbose_name_plural = "fotki claydera" #ikinci tablo(çoğul) adı / a table name in plural form

