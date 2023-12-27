from django.db import models
from jsonfield import JSONField

# Create your models here.
class Character(models.Model):
    # Dnd characters need a lot of things, but we're start with the basic for now
    # A level, class, health, ability scores, movement, name, race
    # Skill proficiencies, gear, feats / class features, spells
    level = models.IntegerField(default=1)
    char_class = models.CharField(max_length=255)
    health = models.IntegerField(default=1)
    movement = models.IntegerField(default=30)
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    ability = JSONField()
