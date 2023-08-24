from django.db import models

class table_user(models.Model):
    first_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    
    class Meta:
        db_table='table_user'
