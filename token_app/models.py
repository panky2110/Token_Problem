from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Token(models.Model):

    created_time = models.DateTimeField(default=datetime.datetime.now())
    token_name = models.CharField(max_length=80, unique=True, db_index=True)
    is_assigned = models.BooleanField(default=False)
    assigned_at = models.DateTimeField(default=timezone.now())
    assigned_alive=models.BooleanField(default=False)
    is_alive = models.BooleanField(default=False)


    class Meta:
        db_table='Token'



