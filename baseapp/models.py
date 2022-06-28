from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=9)
    mobile_no = models.CharField(max_length=15, default='+91 98765 43210')
    grad_year = models.CharField(max_length=4)
    address = models.TextField(max_length=500, default='address')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.reg_no + " " + self.name