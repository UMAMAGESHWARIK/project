from django.db import models


class carbonregister(models.Model):
    name=models.CharField(max_length=20)
    emailid=models.EmailField(unique=True)
    address=models.CharField(max_length=20)
    phoneno= models.CharField(null=True,max_length=11)
    password=models.CharField(max_length=20)
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    login = models.BooleanField(default=False)
    logout = models.BooleanField(default=True)


class carbondataset(models.Model):
    mProduct = models.CharField(max_length=50, null=True)
    Netcontent = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    Netweight = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    manufactureprocess = models.CharField(max_length=255, null=True)
    RawMaterials = models.CharField(max_length=255, null=True)
    Recyclingprocess = models.CharField(max_length=255, null=True)
