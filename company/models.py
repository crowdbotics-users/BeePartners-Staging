from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Company(models.Model):
    COMPANY = models.CharField(max_length=255, blank=True, null=True)
    TIMESTAMP = models.DateTimeField(blank=True, null=True)
    CUSTOM_FLD_IDS = models.TextField(null=True)
    CUSTOM_FLD_DATA = models.TextField(null=True)
    STAGE_CODE = models.CharField(max_length=255, blank=True, null=True)
    STAGE_DESC = models.CharField(max_length=255, blank=True, null=True)
    USER_CODE = models.IntegerField(null=True)
    NOTES = models.TextField(null=True)
    PW_LINK = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.COMPANY)

    class Meta:
        db_table = "companies"

