from django.db import models



# Create your models here.
 
class course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    start_date =models.DateField()
    end_date =models.DateField()
    capacity =models.IntegerField()

    def __str__(self):
        return self.title
    



    

