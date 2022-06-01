from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

RAMSizeGB = (
    ("4", "4"),
    ("8", "8"),
    ("16", "16"),
)
StorageSizeGB = (
    ("20", "20"),
    ("40", "40"),
    ("72", "72")
)

vCPUCoresCount = (
    ("2", "2"),
    ("4", "4"),
    ("6", "6")
)


class ComputationResourceType(models.Model):
    partnumber = models.IntegerField(primary_key=True, verbose_name="Part Number")
    ramsizegb = models.IntegerField(choices=RAMSizeGB, verbose_name="Ram")
    storagesizegb = models.IntegerField(choices=StorageSizeGB, verbose_name="Storage")
    vcpucorescount = models.IntegerField(choices=vCPUCoresCount, verbose_name="CPU cores")
    firmwareversion_regex = RegexValidator(regex=r'^[0-9]{3}.[a-zA-Z]{3}$')
    firmwarversion = models.CharField(validators=[firmwareversion_regex], max_length=10, verbose_name="Firmware Version")
    hardwareversion_regex = RegexValidator(regex=r'^[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{3}[0-9]{2}$')
    hardwarversion = models.CharField(validators=[hardwareversion_regex], max_length=10, verbose_name="Hardware Version")


class Customer(models.Model):
    name_regex = RegexValidator(regex=r'^[a-z A-Z_]{10,82}$')
    name = models.CharField(validators=[name_regex], max_length=82, null=False,primary_key=True)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    email_ID = models.EmailField(max_length=50, unique=True)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=14, blank=False, unique=True)


class ComputationResource(models.Model):
    name_regex = RegexValidator(regex=r'^[a-z A-Z_]{10,82}$')
    name = models.CharField(validators=[name_regex], max_length=82, null=False, primary_key=True)
    part_number = models.ForeignKey(ComputationResourceType, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
