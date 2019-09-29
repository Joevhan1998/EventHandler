from django.db import models

# Create your models here.
class Category(models.Model) :

    name                = models.CharField(max_length=200)

    class Meta:
        ordering        = ('name',)

    def __str__(self) :
        return self.name

class Event(models.Model) :
    STATUS              = {
        ('O',     'Open'),
        ('C',     'Closed'),
    }
    name                = models.CharField(max_length=200)
    start_date_time     = models.DateTimeField()
    end_date_time       = models.DateTimeField()
    max_participants    = models.PositiveIntegerField(blank=True) 
    min_participants    = models.PositiveIntegerField(blank=True) 
    descriptions        = models.TextField()
    status              = models.CharField(max_length=1,choices=STATUS,default = 'O')
    category            = models.ManyToManyField(Category)
    organizer_name      = models.CharField(max_length=200)
    def __str__(self) :
        return self.name


class Register(models.Model) :

    event_id            = models.ForeignKey('Event',on_delete = models.CASCADE)
    participant_id      = models.IntegerField()
    attendance          = models.BooleanField()
    feedback            = models.TextField()



