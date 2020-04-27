from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    next = models.IntegerField(default=-1)

    STATE_NEW = 0
    STATE_INPROGRESS = 1
    STATE_DONE = 2
    STATE_CHOICES = (
        (STATE_NEW, 'New'),
        (STATE_INPROGRESS, 'In Progress'),
        (STATE_DONE, 'Done'),
    ) 
    state = models.SmallIntegerField(choices=STATE_CHOICES, default=STATE_NEW, )

    readonly_fields = ('state',)

