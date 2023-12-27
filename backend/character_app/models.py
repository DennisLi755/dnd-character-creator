from django.db import models
from jsonfield import JSONField
from .validators import validate_name

# Create your models here.
class Character(models.Model):
    # Dnd characters need a lot of things, but we're start with the basic for now
    # A level, class, health, ability scores, movement, name, race
    # Skill proficiencies, gear, feats / class features, spells
    level = models.IntegerField(default=1)
    char_class = models.CharField(max_length=255)
    health = models.IntegerField(default=1)
    movement = models.IntegerField(default=30)
    name = models.CharField(max_length=255, validators=[validate_name])
    race = models.CharField(max_length=255)
    ability = JSONField()
