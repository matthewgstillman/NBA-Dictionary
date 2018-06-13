from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=38)
    team_name = models.CharField(max_length=38)
    primary_color = models.CharField(max_length=38)
    secondary_color = models.CharField(max_length=38)
    third_color = models.CharField(max_length=38)
    primary_hex = models.CharField(max_length=38)
    secondary_hex = models.CharField(max_length=38)
    third_hex = models.CharField(max_length=38)
    website = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = TeamManager()
# Create your models here.
    def __unicode__(self):
        return "id: " + str(self.id) + ", City: " + str(self.city) + ", Team: " + str(self.team_name) + ", Primary Color: " + str(self.primary_color) + ", Secondary Color: " + str(self.secondary_color) + ", Third Color: " + str(self.third_color) + ", Primary Hex Color: " + str(self.primary_hex) + ", Secondary Hex Color: " + str(self.secondary_hex) + ", Third Hex Color: " + str(self.third_hex) 

