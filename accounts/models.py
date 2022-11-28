from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.
class ToDoList(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    # user =models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dardate=models.DateField(default=timezone.now);
    your_day = models.CharField(max_length=50000,default=' ')

    def __str__(self):
        # l=len(self.your_day)
        # if l>20:
	       #  return self.your_day[:20]
        # else :
        #     return self.your_day
        return str(self.dardate)


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
	    return self.text
class date(models.Model):
    choose_date=models.DateField()