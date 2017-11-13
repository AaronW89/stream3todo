from django.db import models

class TodoItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
    
    def __str__(self):
        status = "D" if self.done else "N"        
        return "{0} ({1})".format(self.name, status)