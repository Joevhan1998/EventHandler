from django.db import models

# Create your models here.
class Category(models.Model) :

    name                = models.CharField(max_length=200)

    class Meta:
        ordering        = ('name',)

    def __str__(self) :
        return self.name
"""
class Event(models.Model) :

    name                = models.CharField(max_length=200)
    start_date_time     = models.DateTimeField()
    max_participants    = models.PositiveIntegerField(blank=True) 
    min_participants    = models.PositiveIntegerField(blank=True) 
    descriptions        = models.TextField()
    status              = models.BooleanField()
    category            = models.ManyToManyField(Category)
    organizer_name      = models.ForeignKey('')


    def __str__(self) :
        return self.name


class Register(models.Model) :

    event_id            = models.ForeignKey('Event')
    participant_id      = models.ForeignKey()
    attendance          = models.BooleanField()
    feedback            = models.TextField()
"""


