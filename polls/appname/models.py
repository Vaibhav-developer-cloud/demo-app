from django.db import models

# Create your models here.
class employee(models.Model):
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        contact =models.IntegerField()
        age = models.IntegerField()

class Team(models.Model):
        Team_name =models.CharField(max_length=200)
        TEAM_LEVELS = (("u01","top1"),
                        ("u02","top2")
                       )
        team_level = models.CharField(max_length=5,default="u03",choices=TEAM_LEVELS)

