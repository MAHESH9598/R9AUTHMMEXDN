from django.db import models
class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=10)
    pcost=models.DecimalField(max_digits=10,decimal_places=4)
    pmfdt=models.DateField()
    pexpdt=models.DateField()


# Create your models here.
